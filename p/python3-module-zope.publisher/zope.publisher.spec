%define _unpackaged_files_terminate_build 1
%define pypi_name zope.publisher
%define ns_name zope
%define mod_name publisher

%def_with check

Name: python3-module-%pypi_name
Version: 8.1
Release: alt1
Epoch: 1
Summary: The Zope publisher publishes Python objects on the web
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.publisher/
Vcs: https://github.com/zopefoundation/zope.publisher
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# merged into main
Provides: python3-module-zope.publisher-tests = %EVR
Obsoletes: python3-module-zope.publisher-tests <= 1:7.3-alt1.1
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
# switched to native namespace
Requires: python3-module-zope >= 3.3.0-alt10
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
zope.publisher allows you to publish Python objects on the web. It has
support for plain HTTP/WebDAV clients, web browsers as well as XML-RPC
and FTP clients. Input and output streams are represented by request and
response objects which allow for easy client interaction from Python.
The behaviour of the publisher is geared towards WSGI compatibility.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/

%changelog
* Tue Jun 30 2026 Stanislav Levin <slev@altlinux.org> 1:8.1-alt1
- 8.0 -> 8.1

* Mon Dec 01 2025 Stanislav Levin <slev@altlinux.org> 1:8.0-alt1
- 7.3 -> 8.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 1:7.3-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Thu Mar 06 2025 Stanislav Levin <slev@altlinux.org> 1:7.3-alt1
- 7.2 -> 7.3.

* Fri Dec 20 2024 Stanislav Levin <slev@altlinux.org> 1:7.2-alt1
- 7.1 -> 7.2.

* Fri Sep 27 2024 Stanislav Levin <slev@altlinux.org> 1:7.1-alt1
- 7.0 -> 7.1.

* Fri Mar 15 2024 Stanislav Levin <slev@altlinux.org> 1:7.0-alt1
- 6.1.0 -> 7.0.

* Tue Aug 08 2023 Stanislav Levin <slev@altlinux.org> 1:6.1.0-alt1
- 6.0.1 -> 6.1.0.

* Wed May 26 2021 Grigory Ustinov <grenka@altlinux.org> 1:6.0.1-alt1
- Automatically updated to 6.0.1.

* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 1:5.1.1-alt1
- NMU: 4.3.2 -> 5.1.1
- Remove python2 module build
- Remove ubt tag from changelog
- Enable check
- Remove obsolete fix-tests patch

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.3.2-alt4
- NMU: remove rpm-build-ubt from BR:

* Tue Apr 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:4.3.2-alt3
- requires for tests fixed

* Thu Mar 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:4.3.2-alt2
- Tests fixed

* Mon Mar 05 2018 Stanislav Levin <slev@altlinux.org> 1:4.3.2-alt1
- 4.2.1 -> 4.3.2

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.2.1-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.2.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.2.1-alt1
- Version 4.2.1

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.0-alt1
- Version 4.1.0

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.0-alt2
- Version 4.0.0

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.0-alt1.a4
- Version 4.0.0a4 again

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.13.4-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.13.4-alt1
- Version 3.13.4

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a4
- Version 4.0.0a4

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.0-alt1
- Version 3.13.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.6-alt4.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt1
- Initial build for Sisyphus

