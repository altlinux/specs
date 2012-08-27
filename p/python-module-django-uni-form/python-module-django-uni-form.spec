%define module_name django-uni-form

Name: python-module-%module_name
Version: 0.9.0
Release: alt1.qa1

Summary: The best way to have Django_ DRY forms. Build programmatic reusable layouts out of components, having full control of the rendered HTML

License: BSD
Group: Development/Python
Url: https://github.com/pydanny/django-uni-form.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires: python-module-distribute

%setup_python_module %module_name

%description
Django_ forms are easily rendered as tables, paragraphs, and unordered lists. 
However, elegantly rendered div based forms is something you have to do by hand. 
The purpose of this application is to provide a simple tag and/or filter that
lets you quickly render forms in a div format

%prep
%setup
%patch -p1

%build
%python_build

%install
%python_install

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%files
%doc README* CHANGELOG CONTRIBUTORS.txt LICENSE.txt docs
%python_sitelibdir/uni_form*
%python_sitelibdir/django_uni_form*

%changelog
* Mon Aug 27 2012 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * macos-ds-store-file-in-package for python-module-django-uni-form

* Thu Apr 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.0-alt1
- Initial build for ALT Linux
