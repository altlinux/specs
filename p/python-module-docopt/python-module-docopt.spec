Name: python-module-docopt
Version: 0.6.1
Release: alt1

Summary: Pythonic argument parser, that will make you smile

License: MIT
Group: File tools
Url: https://github.com/docopt/docopt

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/d/docopt/docopt-%version.tar

BuildArch: noarch

# buildreq add all packages :)
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-nose

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
%python_build

%install
%python_install

%files
%python_sitelibdir/docopt.py*
%python_sitelibdir/docopt-*.egg-info

%changelog
* Sat Feb 23 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Sat Feb 16 2013 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- initial build for ALT Linux Sisyphus

* Mon Jan 14 2013 Martin Sivak <msivak@euryale.brq.redhat.com> - 0.5.0-1
- Inital release
