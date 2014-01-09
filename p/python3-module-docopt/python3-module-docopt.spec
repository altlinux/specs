Name: python3-module-docopt
Version: 0.6.1
Release: alt1

Summary: Pythonic argument parser, that will make you smile

License: MIT
Group: File tools
Url: https://github.com/docopt/docopt

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/d/docopt/docopt-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# buildreq add all packages :)
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-nose

%description
Isn't it awesome how optparse and argparse generate help messages
based on your code?!

Hell no! You know what's awesome? It's when the option parser is
generated based on the beautiful help message that you write yourself!
This way you don't need to write thisstupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.

%prep
%setup -n docopt-%version

# remove upstream egg-info
rm -rf *.egg-info

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/docopt.py*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/docopt-*.egg-info

%changelog
* Fri Jan 10 2014 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- initial build for ALT Linux Sisyphus
