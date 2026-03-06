%define _unpackaged_files_terminate_build 1
%define pypi_name dnspython
%define mod_name dns

# Testing requires network access
%def_with check

%define add_pyproject_extra() \
%{expand:%%package -n python3-module-%%{pep503_name %%pypi_name}+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: python3-module-%%{pep503_name %%pypi_name} = %%EVR \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n python3-module-%%{pep503_name %%pypi_name}+%1 \
Extra "%1" for %%pypi_name. \
%%files -n python3-module-%%{pep503_name %%pypi_name}+%1 \
}

Name: python3-module-%mod_name
Version: 2.8.0
Release: alt1
Epoch: 1
Summary: DNS toolkit
License: ISC
Group: Development/Python
Url: https://pypi.org/project/dnspython/
Vcs: https://github.com/rthalley/dnspython
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%py3_provides %pypi_name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra dev
%pyproject_builddeps_metadata_extra doh
%pyproject_builddeps_metadata_extra dnssec
%pyproject_builddeps_metadata_extra idna
%pyproject_builddeps_metadata_extra trio
%pyproject_builddeps_metadata_extra doq
%endif

# extra functionality
%add_pyproject_extra doh
%add_pyproject_extra dnssec
%add_pyproject_extra idna
%add_pyproject_extra trio
%add_pyproject_extra doq

%description
dnspython is a DNS toolkit for Python. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates.  It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set.  The low level classes allow
direct manipulation of DNS zones, messages, names, and records.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Mar 06 2026 Stanislav Levin <slev@altlinux.org> 1:2.8.0-alt1
- 2.6.1 -> 2.8.0.

* Sat Mar 02 2024 Vitaly Lipatov <lav@altlinux.ru> 1:2.6.1-alt1
- new version 2.6.1, change license to ISC
- switch to pyproject_build
- CVE-2023-29483

* Sat May 06 2023 Anton Zhukharev <ancieg@altlinux.org> 1:2.2.0-alt2
- (NMU) Added missing provides.

* Sat Feb 12 2022 Anton Midyukov <antohami@altlinux.org> 1:2.2.0-alt1
- new version (2.2.0) with rpmgs script
- enable check

* Wed Nov 18 2020 Vitaly Lipatov <lav@altlinux.ru> 1:1.16.0-alt2
- return to 1.16.0 due https://github.com/eventlet/eventlet/issues/619

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1.16.0-alt1
- new version 1.16.0 (with rpmrb script)
- build from tarball
- no more doc build

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.15.0-alt2
- NMU: rebuilt with python-3.6.

* Wed Jul 12 2017 Terechkov Evgenii <evg@altlinux.org> 1.15.0-alt1
- 1.15.0

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.12.0-alt1.git20150613.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.12.0-alt1.git20150613.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.0-alt1.git20150613
- Version 1.12.0

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.1-alt1.git20140411
- New snapshot

* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.1-alt1.git20130902
- Version 1.11.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.10.0-alt2
- Version 1.10.0 (py3)
- Build for Python-3
- Rename package to python3-module-dns

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.10.0-alt2
- Version 1.10.0
- Obsoletes python-module-dnspython (ALT #28727)

* Sun Oct 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.2-alt1.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.2-alt1
- Version 1.9.2

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- cleanup spec
- new version (1.8.0) import in git

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.3.4-alt1.1
- Rebuilt with python-2.5.

* Mon Oct 03 2005 Andrey Orlov <cray@altlinux.ru> 1.3.4-alt1
- initial release

