Name:       docopts
Version:    0.6.1
Release:    alt2

Summary:    shell interface for docopt, the CLI description language
License:    MIT
Group:      Development/Python3
Url:        https://github.com/docopt/docopts

BuildArch:  noarch

Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-docopt


%description
docopts parses the command line argument vector argv according
to the docopt string msg and echoes the results to standard
output as a snippet of Bash source code. Passing this snippet
as an argument to eval(1) is sufficient for handling the CLI
needs of most scripts.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name
%python3_sitelibdir/*


%changelog
* Thu Jan 30 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt2
- Porting on Python3.

* Sat Feb 16 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- Initial build for ALTLinux Sisyphus

