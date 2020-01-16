%define  modulename psycogreen

Name:    python3-module-%modulename
Version: 1.0.1
Release: alt2

Summary: psycopg2 integration with coroutine libraries

License: BSD
Group:   Development/Python3
URL:     https://bitbucket.org/dvarrazzo/psycogreen
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Source:  %modulename-%version.tar


%description
The psycogreen package enables psycopg2 to work with coroutine
libraries, using asynchronous calls internally but offering a blocking
interface so that regular code can run unmodified.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info


%changelog
* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt2
- porting on python3

* Mon Oct 07 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- New version.

* Tue Jan 10 2017 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
