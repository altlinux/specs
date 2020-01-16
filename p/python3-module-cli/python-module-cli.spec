%define oname cli

Name:    python3-module-cli
Version: 1.2
Release: alt4

Summary: A CLI construction toolkit for Python
License: MIT
Group:   Development/Python3
URL:     https://bitbucket.org/geertj/python-cli/wiki/Home

BuildArch: noarch

Source0: https://bitbucket.org/geertj/python-cli/get/python-cli-%{version}.tar.gz
Patch0:  fix-import.patch

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-module-ply python-tools-2to3

Provides: python3-cli = %version-%release


%description
This is Python-CLI, a CLI construction toolkit for Python.
It is similar in scope to Python's "cmd", "cmd2", and pyCLI.

%prep
%setup -q -n geertj-python-cli-a59ff13ea99d
%patch0 -p2

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS README LICENSE
%_bindir/cli-test
%python3_sitelibdir/*


%changelog
* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2-alt4
- porting on python3

* Thu Feb 11 2016 Denis Medvedev <nbr@altlinux.org> 1.2-alt3
- Fix based on redhat's ovirt bugzilla

* Thu Mar 27 2014 Andrey Cherepanov <cas@altlinux.org> 1.2-alt2
- Rebuild to prevent autoimports conflict

* Wed Mar 26 2014 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Initial build for ALT Linux
