%define oname tldextract

%def_with check

Name: python3-module-%oname
Version: 5.0.1
Release: alt1

Summary: Accurately separate the TLD from the registered domain and subdomains of a URL

License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/tldextract
VCS: https://github.com/john-kurkowski/tldextract

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-requests-file
BuildRequires: python3-module-responses
BuildRequires: python3-module-pytest-mock
%endif

%py3_provides %oname

%description
tldextract accurately separates the gTLD or ccTLD (generic or country
code top-level domain) from the registered domain and subdomains of a
URL, using the Public Suffix List.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
# deprecated code check, see task #307207
sed -i 's/--pylint//g' tox.ini
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%tox_check_pyproject

%files
%doc *.md
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Oct 24 2023 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt1
- Automatically updated to 5.0.1.

* Thu Sep 21 2023 Grigory Ustinov <grenka@altlinux.org> 3.6.0-alt1
- Automatically updated to 3.6.0.

* Thu Sep 07 2023 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- Automatically updated to 3.5.0.

* Mon Jun 12 2023 Grigory Ustinov <grenka@altlinux.org> 3.4.4-alt1
- Automatically updated to 3.4.4.

* Wed May 17 2023 Grigory Ustinov <grenka@altlinux.org> 3.4.2-alt1
- Automatically updated to 3.4.2.

* Fri Apr 28 2023 Grigory Ustinov <grenka@altlinux.org> 3.4.1-alt1
- Automatically updated to 3.4.1.

* Thu Oct 06 2022 Grigory Ustinov <grenka@altlinux.org> 3.4.0-alt1
- Automatically updated to 3.4.0.
- Build with check.

* Sat Jul 16 2022 Grigory Ustinov <grenka@altlinux.org> 3.3.1-alt1
- Automatically updated to 3.3.1.

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- Automatically updated to 3.3.0.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1.git20141205.3
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.5.1-alt1.git20141205.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.1-alt1.git20141205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.1-alt1.git20141205.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git20141205
- Initial build for Sisyphus

