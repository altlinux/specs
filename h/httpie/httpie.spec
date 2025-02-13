%define _unpackaged_files_terminate_build 1
%define pypi_name httpie

%def_with check

Name: httpie
Version: 3.2.4
Release: alt3

Summary: HTTPie: modern, user-friendly command-line HTTP client for the API era
Group: Networking/WWW
License: BSD
Url: http://httpie.org
VCS: https://github.com/httpie/cli.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pygments
BuildRequires: python3-module-requests_toolbelt
BuildRequires: python3-module-rich
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-multidict
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-httpbin
BuildRequires: python3-module-responses
BuildRequires: python3-module-pytest-mock
%endif

%description
HTTPie is a CLI HTTP utility built out of frustration with existing tools. The
goal is to make CLI interaction with HTTP-based services as human-friendly as
possible.

HTTPie does so by providing an http command that allows for issuing arbitrary
HTTP requests using a simple and natural syntax and displaying colorized
responses.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
##https://github.com/httpie/cli/issues/1276#issuecomment-1019441082
%pyproject_run_pytest -m "not requires_installation"

%files
%_bindir/http
%_bindir/httpie
%_bindir/https
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%{version}*
%_man1dir/http.1*
%_man1dir/https.1*
%_man1dir/httpie.1*
%doc LICENSE README.md

%changelog
* Wed Jan 22 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.2.4-alt3
- New version 3.2.4
- Updated build system
  + enable tests

* Mon Dec 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt3
- Updated runtime dependencies.

* Fri Dec 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt2
- Updated obsoletes.
- Stopped renaming binaries and man pages.

* Wed Dec 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Updated to upstream version 2.3.0 (Fixes: CVE-2019-10751).

* Sat Dec 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.9-alt2
- build for python2 disabled

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1.qa1
- NMU: applied repocop patch

* Fri Sep 21 2018 Terechkov Evgenii <evg@altlinux.org> 0.9.9-alt1
- 0.9.9

* Wed Jul 18 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.8-alt3
- Fixed FTBFS (Add BR python3-module-setuptools).

* Wed Jul 19 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.8-alt2
- Update requires
- Added patch - fixed import 'urllib3'

* Wed Jul 19 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.8-alt1
- Build new version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Sep  6 2014 Terechkov Evgenii <evg@altlinux.org> 0.8.0-alt1
- Initial build for ALT Linux Sisyphus
