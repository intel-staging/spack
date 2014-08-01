# FIXME: Add copyright

from spack import *
import os

class Otf2(Package):
    """The Open Trace Format 2 is a highly scalable, memory efficient event
       trace data format plus support library."""

    homepage = "http://www.vi-hps.org/score-p"
    url      = "http://www.vi-hps.org/upload/packages/otf2/otf2-1.4.tar.gz"

    version('1.4',   'a23c42e936eb9209c4e08b61c3cf5092',
            url="http://www.vi-hps.org/upload/packages/otf2/otf2-1.4.tar.gz")
    version('1.3.1', 'd0ffc4e858455ace4f596f910e68c9f2',
            url="http://www.vi-hps.org/upload/packages/otf2/otf2-1.3.1.tar.gz")
    version('1.2.1', '8fb3e11fb7489896596ae2c7c83d7fc8',
            url="http://www.vi-hps.org/upload/packages/otf2/otf2-1.2.1.tar.gz")


    @when('@:1.2')
    def version_specific_args(self, args):
        return ["--with-platform=disabled"]

    @when('@1.3:')
    def version_specific_args(self, args):
        # TODO: figure out what scorep's build does as of otf2 1.3
        return []


    def install(self, spec, prefix):
        # FIXME: Modify the configure line to suit your build system here.
        cc = os.environ["SPACK_CC"]

        configure_args=["--prefix=%s" % prefix,
                        "--enable-shared"])

        configure_args.extend(self.version_specific_args())

        configure(*configure_args)

        # FIXME: Add logic to build and install here
        make()
        make("install")
