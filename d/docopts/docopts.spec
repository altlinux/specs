Name: docopts
Version: 0.6.1
Release: alt1

Summary: shell interface for docopt, the CLI description language

License: MIT
Group: Development/Python
Url: https://github.com/docopt/docopts

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools python-module-docopt

%description
docopts parses the command line argument vector argv according
to the docopt string msg and echoes the results to standard
output as a snippet of Bash source code. Passing this snippet
as an argument to eval(1) is sufficient for handling the CLI
needs of most scripts.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/%name
%python_sitelibdir/*

%changelog
* Sat Feb 16 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- Initial build for ALTLinux Sisyphus

