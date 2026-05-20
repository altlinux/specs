%define _unpackaged_files_terminate_build 1

%define pypi_name django-ckeditor
%define mod_name ckeditor

%def_with check

Name: python3-module-%pypi_name
Version: 6.7.3
Release: alt1

Summary: Django admin CKEditor integration
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-ckeditor/
VCS: https://github.com/shaunsephton/django-ckeditor.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3(coverage)
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-django
BuildRequires: python3-module-django-extensions
BuildRequires: python3-module-django-js-asset
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-selenium
%endif

%add_python3_req_skip selenium
%add_python3_req_skip selenium.webdriver.common.by

%description
Django admin CKEditor integration. Provides a RichTextField,
RichTextUploadingField, CKEditorWidget and CKEditorUploadingWidget
utilizing CKEditor with image upload and browsing support included.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

rm -rf %buildroot%python3_sitelibdir/%mod_name-%version/docs

%check
%tox_check_pyproject

%files
%doc *.rst LICENSE
%python3_sitelibdir/%mod_name
%python3_sitelibdir/ckeditor_uploader
%python3_sitelibdir/ckeditor_demo
%python3_sitelibdir/django_ckeditor-%version.dist-info


%changelog
* Wed May 20 2026 Anton Vyatkin <toni@altlinux.org> 6.7.3-alt1
- New version 6.7.3.

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 6.7.2-alt2.1
- Demodernized packaging.

* Tue May 06 2025 Dmitry Lyalyaev <fruktime@altlinux.org> 6.7.2-alt2
- remove the Selenium dependency

* Tue Apr 30 2025 Dmitry Lyalyaev <fruktime@altlinux.org> 6.7.2-alt1
- 6.4.1 -> 6.7.2

* Fri May 30 2022 Dmitry Lyalyaev <fruktime@altlinux.org> 6.4.1-alt1
- New version.

* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 5.6.1-alt2
- build for python2 disabled

* Mon Dec 24 2018 Grigory Ustinov <grenka@altlinux.org> 5.6.1-alt1
- Build new version.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.4.6-alt1.git20140923.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.6-alt1.git20140923.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.6-alt1.git20140923
- Initial build for Sisyphus
