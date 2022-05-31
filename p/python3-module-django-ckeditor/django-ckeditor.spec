%define _unpackaged_files_terminate_build 1

%define oname django-ckeditor

Name: python3-module-%oname
Version: 6.4.1
Release: alt1

Summary: Django admin CKEditor integration
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-ckeditor/
BuildArch: noarch

# VCS: https://github.com/shaunsephton/django-ckeditor.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django-js-asset

%add_python3_req_skip selenium

%description
Django admin CKEditor integration. Provides a RichTextField,
RichTextUploadingField, CKEditorWidget and CKEditorUploadingWidget
utilizing CKEditor with image upload and browsing support included.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
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

