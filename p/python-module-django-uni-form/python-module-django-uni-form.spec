%define module_name django-uni-form

%def_with python3

Name: python-module-%module_name
Version: 0.9.0
Release: alt2.1

Summary: The best way to have Django_ DRY forms. Build programmatic reusable layouts out of components, having full control of the rendered HTML

License: BSD
Group: Development/Python
Url: https://github.com/pydanny/django-uni-form.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%setup_python_module %module_name

%description
Django_ forms are easily rendered as tables, paragraphs, and unordered lists. 
However, elegantly rendered div based forms is something you have to do by hand. 
The purpose of this application is to provide a simple tag and/or filter that
lets you quickly render forms in a div format

%package -n python3-module-%module_name
Summary: The best way to have Django_ DRY forms. Build programmatic reusable layouts out of components, having full control of the rendered HTML
Group: Development/Python3

%description -n python3-module-%module_name
Django_ forms are easily rendered as tables, paragraphs, and unordered lists. 
However, elegantly rendered div based forms is something you have to do by hand. 
The purpose of this application is to provide a simple tag and/or filter that
lets you quickly render forms in a div format

%prep
%setup
%patch -p1

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%files
%doc README* CHANGELOG CONTRIBUTORS.txt LICENSE.txt docs
%python_sitelibdir/uni_form*
%python_sitelibdir/django_uni_form*

%if_with python3
%files -n python3-module-%module_name
%doc README* CHANGELOG CONTRIBUTORS.txt LICENSE.txt docs
%python3_sitelibdir/uni_form*
%python3_sitelibdir/django_uni_form*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt2
- Added module for Python 3

* Mon Aug 27 2012 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * macos-ds-store-file-in-package for python-module-django-uni-form

* Thu Apr 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.0-alt1
- Initial build for ALT Linux
