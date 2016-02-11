
Name:	 python-module-cli
Version: 1.2
Release: alt3
Summary: A CLI construction toolkit for Python

License: MIT
Group:   Development/Python
URL:     https://bitbucket.org/geertj/python-cli/wiki/Home
Source0: https://bitbucket.org/geertj/python-cli/get/python-cli-%{version}.tar.gz

BuildArch:      noarch

Provides: python-cli = %version-%release

BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-distribute
BuildRequires:  python-module-ply

%description
This is Python-CLI, a CLI construction toolkit for Python.
It is similar in scope to Python's "cmd", "cmd2", and pyCLI.

%prep
%setup -q -n geertj-python-cli-a59ff13ea99d

%build
%python_build

%install
%python_install

%files
%doc AUTHORS README LICENSE
%_bindir/cli-test
%python_sitelibdir/*

%changelog
* Thu Feb 11 2016 Denis Medvedev <nbr@altlinux.org> 1.2-alt3
- Fix based on redhat's ovirt bugzilla

* Thu Mar 27 2014 Andrey Cherepanov <cas@altlinux.org> 1.2-alt2
- Rebuild to prevent autoimports conflict

* Wed Mar 26 2014 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Initial build for ALT Linux
