%define oname tqdm

%def_with check

Name: python3-module-tqdm
Version: 4.66.1
Release: alt1

Summary: A fast, extensible progress bar for Python and CLI

License: MIT and MPL-2.0
Group: Development/Python
Url: https://pypi.org/project/tqdm

Source: %name-%version.tar

BuildArch: noarch

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-numpy
%endif

# make optional
%add_python3_req_skip dask.callbacks rich.progress

%description
tqdm means "progress" in Arabic (taqadum) and an abbreviation
for "I love you so much" in Spanish (te quiero demasiado).

Instantly make your loops show a smart progress meter -
just wrap any iterable with tqdm(iterable), and you're done!

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc *.rst
%_bindir/tqdm
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Tue Sep 26 2023 Anton Vyatkin <toni@altlinux.org> 4.66.1-alt1
- new version 4.66.1

* Wed Apr 12 2023 Anton Vyatkin <toni@altlinux.org> 4.65.0-alt2
- Fix BuildRequires

* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 4.65.0-alt1
- new version 4.65.0 (with rpmrb script)

* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 4.64.1-alt1
- new version 4.64.1 (with rpmrb script)

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 4.64.0-alt1
- new version 4.64.0 (with rpmrb script)

* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 4.63.1-alt1
- new version 4.63.1 (with rpmrb script)

* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 4.62.2-alt1
- new version 4.62.2 (with rpmrb script)

* Thu Aug 26 2021 Vitaly Lipatov <lav@altlinux.ru> 4.62.1-alt1
- new version 4.62.1 (with rpmrb script)

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 4.62.0-alt2
- make dask, rich module requirement optional

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 4.62.0-alt1
- new version 4.62.0 (with rpmrb script)

* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.48.0-alt1
- 4.48.0 released

* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 4.42.1-alt2
- add conflicts/obsoletes for python-module-tqdm (due bindir/tqdm)

* Fri Feb 07 2020 Vitaly Lipatov <lav@altlinux.ru> 4.42.1-alt1
- build separate python3 module
- new version 4.42.1 (with rpmrb script)

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.15.0-alt1
- Initial build for ALT.
