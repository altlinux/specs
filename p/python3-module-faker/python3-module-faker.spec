%define  oname faker

%def_with check

Name:    python3-module-%oname
Version: 28.4.1
Release: alt1

Summary: Faker is a Python package that generates fake data for you.

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/Faker
VCS:     https://github.com/joke2k/faker

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-text-unidecode
BuildRequires: python3-module-validators
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-random2
%endif

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
# Exclude tests that require the faker.sphinx module
py.test3 --ignore-glob='tests/sphinx/*'

%files
%doc LICENSE.txt *.rst *.md
%_bindir/%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/Faker-%version-py%_python3_version.egg-info

%changelog
* Tue Sep 10 2024 Grigory Ustinov <grenka@altlinux.org> 28.4.1-alt1
- Automatically updated to 28.4.1.

* Thu Aug 15 2024 Grigory Ustinov <grenka@altlinux.org> 27.0.0-alt1
- Automatically updated to 27.0.0.

* Tue Aug 06 2024 Grigory Ustinov <grenka@altlinux.org> 26.2.0-alt1
- Automatically updated to 26.2.0.

* Fri Aug 02 2024 Grigory Ustinov <grenka@altlinux.org> 26.1.0-alt1
- Automatically updated to 26.1.0.

* Sun Jun 30 2024 Grigory Ustinov <grenka@altlinux.org> 26.0.0-alt1
- Automatically updated to 26.0.0.

* Tue Jun 25 2024 Grigory Ustinov <grenka@altlinux.org> 25.9.1-alt1
- Automatically updated to 25.9.1.

* Fri Jun 14 2024 Grigory Ustinov <grenka@altlinux.org> 25.8.0-alt1
- Automatically updated to 25.8.0.

* Wed Jun 05 2024 Grigory Ustinov <grenka@altlinux.org> 25.5.0-alt1
- Automatically updated to 25.5.0.

* Tue Jun 04 2024 Grigory Ustinov <grenka@altlinux.org> 25.4.0-alt1
- Automatically updated to 25.4.0.

* Tue May 28 2024 Grigory Ustinov <grenka@altlinux.org> 25.3.0-alt1
- Automatically updated to 25.3.0.

* Tue May 14 2024 Grigory Ustinov <grenka@altlinux.org> 25.2.0-alt1
- Automatically updated to 25.2.0.

* Sun May 12 2024 Grigory Ustinov <grenka@altlinux.org> 25.1.0-alt1
- Automatically updated to 25.1.0.

* Tue Apr 30 2024 Grigory Ustinov <grenka@altlinux.org> 25.0.0-alt1
- Automatically updated to 25.0.0.

* Fri Apr 19 2024 Grigory Ustinov <grenka@altlinux.org> 24.11.0-alt1
- Automatically updated to 24.11.0.

* Tue Apr 16 2024 Grigory Ustinov <grenka@altlinux.org> 24.9.0-alt1
- Automatically updated to 24.9.0.

* Tue Apr 09 2024 Grigory Ustinov <grenka@altlinux.org> 24.8.0-alt1
- Automatically updated to 24.8.0.

* Tue Mar 26 2024 Grigory Ustinov <grenka@altlinux.org> 24.4.0-alt1
- Automatically updated to 24.4.0.

* Thu Mar 21 2024 Grigory Ustinov <grenka@altlinux.org> 24.3.0-alt1
- Automatically updated to 24.3.0.

* Mon Mar 18 2024 Grigory Ustinov <grenka@altlinux.org> 24.2.0-alt1
- Automatically updated to 24.2.0.

* Mon Mar 11 2024 Grigory Ustinov <grenka@altlinux.org> 24.1.0-alt1
- Automatically updated to 24.1.0.

* Tue Mar 05 2024 Grigory Ustinov <grenka@altlinux.org> 24.0.0-alt1
- Automatically updated to 24.0.0.

* Fri Mar 01 2024 Grigory Ustinov <grenka@altlinux.org> 23.3.0-alt1
- Automatically updated to 23.3.0.

* Sat Feb 17 2024 Grigory Ustinov <grenka@altlinux.org> 23.2.1-alt1
- Automatically updated to 23.2.1.

* Sat Feb 10 2024 Grigory Ustinov <grenka@altlinux.org> 23.1.0-alt1
- Automatically updated to 23.1.0.

* Wed Feb 07 2024 Grigory Ustinov <grenka@altlinux.org> 23.0.0-alt1
- Automatically updated to 23.0.0.

* Tue Feb 06 2024 Grigory Ustinov <grenka@altlinux.org> 22.7.0-alt1
- Automatically updated to 22.7.0.

* Wed Jan 31 2024 Grigory Ustinov <grenka@altlinux.org> 22.6.0-alt1
- Automatically updated to 22.6.0.

* Wed Jan 24 2024 Grigory Ustinov <grenka@altlinux.org> 22.5.1-alt1
- Automatically updated to 22.5.1.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 22.5.0-alt1
- Automatically updated to 22.5.0.

* Mon Jan 08 2024 Grigory Ustinov <grenka@altlinux.org> 22.1.0-alt1
- Automatically updated to 22.1.0.

* Mon Jan 01 2024 Grigory Ustinov <grenka@altlinux.org> 22.0.0-alt1
- Automatically updated to 22.0.0.

* Mon Dec 25 2023 Grigory Ustinov <grenka@altlinux.org> 21.0.0-alt1
- Automatically updated to 21.0.0.

* Tue Oct 31 2023 Grigory Ustinov <grenka@altlinux.org> 19.12.0-alt1
- Automatically updated to 19.12.0.

* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 19.11.0-alt1
- Automatically updated to 19.11.0.

* Thu Sep 21 2023 Grigory Ustinov <grenka@altlinux.org> 19.6.2-alt1
- Automatically updated to 19.6.2.

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 19.6.1-alt1
- Automatically updated to 19.6.1.

* Mon Sep 11 2023 Grigory Ustinov <grenka@altlinux.org> 19.6.0-alt1
- Automatically updated to 19.6.0.

* Mon Sep 04 2023 Grigory Ustinov <grenka@altlinux.org> 19.3.1-alt1
- Automatically updated to 19.3.1.

* Tue Aug 22 2023 Grigory Ustinov <grenka@altlinux.org> 19.3.0-alt1
- Automatically updated to 19.3.0.

* Mon Jul 24 2023 Grigory Ustinov <grenka@altlinux.org> 19.2.0-alt1
- Automatically updated to 19.2.0.

* Mon Jul 17 2023 Grigory Ustinov <grenka@altlinux.org> 19.1.0-alt1
- Automatically updated to 19.1.0.

* Wed Jul 12 2023 Grigory Ustinov <grenka@altlinux.org> 19.0.0-alt1
- Automatically updated to 19.0.0.

* Fri Jun 30 2023 Grigory Ustinov <grenka@altlinux.org> 18.11.2-alt1
- Automatically updated to 18.11.2.

* Fri Jun 23 2023 Grigory Ustinov <grenka@altlinux.org> 18.11.1-alt1
- Automatically updated to 18.11.1.

* Sun Jun 11 2023 Grigory Ustinov <grenka@altlinux.org> 18.10.1-alt1
- Automatically updated to 18.10.1.

* Wed May 17 2023 Grigory Ustinov <grenka@altlinux.org> 18.9.0-alt1
- Automatically updated to 18.9.0.

* Mon May 15 2023 Grigory Ustinov <grenka@altlinux.org> 18.7.0-alt1
- Automatically updated to 18.7.0.

* Fri May 05 2023 Grigory Ustinov <grenka@altlinux.org> 18.6.2-alt1
- Automatically updated to 18.6.2.

* Wed May 03 2023 Grigory Ustinov <grenka@altlinux.org> 18.6.1-alt1
- Automatically updated to 18.6.1.

* Fri Apr 28 2023 Grigory Ustinov <grenka@altlinux.org> 18.6.0-alt1
- Automatically updated to 18.6.0.

* Tue Apr 25 2023 Grigory Ustinov <grenka@altlinux.org> 18.5.1-alt1
- Automatically updated to 18.5.1.

* Fri Apr 21 2023 Grigory Ustinov <grenka@altlinux.org> 18.4.0-alt1
- New version 18.4.0.

* Fri Mar 24 2023 Grigory Ustinov <grenka@altlinux.org> 18.3.1-alt1
- Automatically updated to 18.3.1.

* Thu Mar 23 2023 Grigory Ustinov <grenka@altlinux.org> 18.3.0-alt1
- Automatically updated to 18.3.0.

* Mon Mar 06 2023 Grigory Ustinov <grenka@altlinux.org> 17.6.0-alt1
- Automatically updated to 17.6.0.

* Thu Mar 02 2023 Grigory Ustinov <grenka@altlinux.org> 17.5.0-alt1
- Automatically updated to 17.5.0.

* Wed Mar 01 2023 Grigory Ustinov <grenka@altlinux.org> 17.4.0-alt1
- Automatically updated to 17.4.0.

* Sun Feb 26 2023 Grigory Ustinov <grenka@altlinux.org> 17.3.0-alt1
- Automatically updated to 17.3.0.

* Tue Feb 14 2023 Grigory Ustinov <grenka@altlinux.org> 17.0.0-alt1
- Automatically updated to 17.0.0.

* Sat Feb 11 2023 Grigory Ustinov <grenka@altlinux.org> 16.8.1-alt1
- Automatically updated to 16.8.1.

* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 16.7.0-alt1
- Automatically updated to 16.7.0.

* Wed Jan 25 2023 Grigory Ustinov <grenka@altlinux.org> 16.6.1-alt1
- Automatically updated to 16.6.1.

* Thu Jan 19 2023 Grigory Ustinov <grenka@altlinux.org> 16.6.0-alt1
- Automatically updated to 16.6.0.

* Fri Jan 13 2023 Grigory Ustinov <grenka@altlinux.org> 16.4.0-alt1
- Automatically updated to 16.4.0.

* Thu Jan 12 2023 Grigory Ustinov <grenka@altlinux.org> 16.3.0-alt1
- Automatically updated to 16.3.0.

* Thu Dec 01 2022 Grigory Ustinov <grenka@altlinux.org> 15.3.4-alt1
- Automatically updated to 15.3.4.

* Tue Nov 29 2022 Grigory Ustinov <grenka@altlinux.org> 15.3.3-alt1
- Automatically updated to 15.3.3.

* Tue Nov 15 2022 Grigory Ustinov <grenka@altlinux.org> 15.3.2-alt1
- Automatically updated to 15.3.2.

* Sat Nov 05 2022 Grigory Ustinov <grenka@altlinux.org> 15.2.0-alt1
- Automatically updated to 15.2.0.

* Thu Nov 03 2022 Grigory Ustinov <grenka@altlinux.org> 15.1.3-alt1
- Automatically updated to 15.1.3.

* Fri Oct 14 2022 Grigory Ustinov <grenka@altlinux.org> 15.1.1-alt1
- Automatically updated to 15.1.1.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 15.1.0-alt1
- Automatically updated to 15.1.0.

* Tue Sep 27 2022 Grigory Ustinov <grenka@altlinux.org> 15.0.0-alt1
- Automatically updated to 15.0.0.

* Sat Sep 24 2022 Grigory Ustinov <grenka@altlinux.org> 14.2.1-alt1
- Automatically updated to 14.2.1.

* Mon Sep 12 2022 Grigory Ustinov <grenka@altlinux.org> 14.2.0-alt1
- Automatically updated to 14.2.0.

* Thu Aug 18 2022 Grigory Ustinov <grenka@altlinux.org> 14.1.0-alt1
- Automatically updated to 14.1.0.

* Fri Aug 12 2022 Grigory Ustinov <grenka@altlinux.org> 14.0.0-alt1
- Automatically updated to 14.0.0.

* Mon Jul 25 2022 Grigory Ustinov <grenka@altlinux.org> 13.15.1-alt1
- Automatically updated to 13.15.1.

* Fri Jul 15 2022 Grigory Ustinov <grenka@altlinux.org> 13.15.0-alt1
- Automatically updated to 13.15.0.

* Fri Jun 24 2022 Grigory Ustinov <grenka@altlinux.org> 13.14.0-alt1
- Automatically updated to 13.14.0.
- Build with check.

* Mon Jun 13 2022 Grigory Ustinov <grenka@altlinux.org> 13.13.0-alt1
- Automatically updated to 13.13.0.

* Tue Jun 07 2022 Grigory Ustinov <grenka@altlinux.org> 13.12.1-alt1
- Automatically updated to 13.12.1.

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 13.12.0-alt1
- Automatically updated to 13.12.0.

* Fri May 20 2022 Grigory Ustinov <grenka@altlinux.org> 13.11.1-alt1
- Automatically updated to 13.11.1.

* Wed May 11 2022 Grigory Ustinov <grenka@altlinux.org> 13.11.0-alt1
- Automatically updated to 13.11.0.

* Thu May 05 2022 Grigory Ustinov <grenka@altlinux.org> 13.7.0-alt1
- Automatically updated to 13.7.0.

* Thu Apr 28 2022 Grigory Ustinov <grenka@altlinux.org> 13.6.0-alt1
- Automatically updated to 13.6.0.

* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 13.4.0-alt1
- Automatically updated to 13.4.0.

* Thu Apr 14 2022 Grigory Ustinov <grenka@altlinux.org> 13.3.4-alt1
- Automatically updated to 13.3.4.

* Thu Mar 24 2022 Grigory Ustinov <grenka@altlinux.org> 13.3.3-alt1
- Automatically updated to 13.3.3.

* Tue Mar 15 2022 Grigory Ustinov <grenka@altlinux.org> 13.3.2-alt1
- Automatically updated to 13.3.2.

* Thu Mar 10 2022 Grigory Ustinov <grenka@altlinux.org> 13.3.1-alt1
- Automatically updated to 13.3.1.

* Sat Feb 05 2022 Grigory Ustinov <grenka@altlinux.org> 12.1.0-alt1
- Automatically updated to 12.1.0.

* Mon Jan 17 2022 Grigory Ustinov <grenka@altlinux.org> 11.3.0-alt1
- Automatically updated to 11.3.0.

* Tue Nov 30 2021 Grigory Ustinov <grenka@altlinux.org> 9.9.0-alt1
- Automatically updated to 9.9.0.

* Tue Nov 23 2021 Grigory Ustinov <grenka@altlinux.org> 9.8.3-alt1
- Automatically updated to 9.8.3.

* Tue Oct 12 2021 Grigory Ustinov <grenka@altlinux.org> 9.3.1-alt1
- Automatically updated to 9.3.1.

* Thu Oct 07 2021 Grigory Ustinov <grenka@altlinux.org> 9.0.0-alt1
- Automatically updated to 9.0.0.

* Tue Sep 07 2021 Grigory Ustinov <grenka@altlinux.org> 8.12.1-alt1
- Automatically updated to 8.12.1.

* Mon Aug 09 2021 Grigory Ustinov <grenka@altlinux.org> 8.11.0-alt1
- Automatically updated to 8.11.0.

* Tue Jul 13 2021 Grigory Ustinov <grenka@altlinux.org> 8.10.1-alt1
- Automatically updated to 8.10.1.

* Wed Jul 07 2021 Grigory Ustinov <grenka@altlinux.org> 8.9.1-alt1
- Automatically updated to 8.9.1.

* Thu Jul 01 2021 Grigory Ustinov <grenka@altlinux.org> 8.9.0-alt1
- Automatically updated to 8.9.0.

* Sun Jun 27 2021 Grigory Ustinov <grenka@altlinux.org> 8.8.2-alt1
- Automatically updated to 8.8.2.

* Fri Jun 18 2021 Grigory Ustinov <grenka@altlinux.org> 8.8.1-alt1
- Automatically updated to 8.8.1.

* Sat Jun 05 2021 Grigory Ustinov <grenka@altlinux.org> 8.5.1-alt1
- Automatically updated to 8.5.1.

* Fri May 28 2021 Grigory Ustinov <grenka@altlinux.org> 8.4.0-alt1
- Automatically updated to 8.4.0.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 8.2.1-alt1
- Automatically updated to 8.2.1.

* Sat May 15 2021 Grigory Ustinov <grenka@altlinux.org> 8.1.4-alt1
- Automatically updated to 8.1.4.

* Wed May 12 2021 Grigory Ustinov <grenka@altlinux.org> 8.1.3-alt1
- Automatically updated to 8.1.3.

* Sun May 09 2021 Grigory Ustinov <grenka@altlinux.org> 8.1.2-alt1
- Automatically updated to 8.1.2.

* Mon Apr 26 2021 Grigory Ustinov <grenka@altlinux.org> 8.1.1-alt1
- Automatically updated to 8.1.1.

* Thu Apr 22 2021 Grigory Ustinov <grenka@altlinux.org> 8.1.0-alt1
- Automatically updated to 8.1.0.

* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 7.0.1-alt1
- Initial build for Sisyphus.
