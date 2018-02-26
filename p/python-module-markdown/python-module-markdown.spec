%define version 2.1.1
%define release alt1
%define modulename markdown

%def_with python3

%setup_python_module %modulename

Name: %packagename
Version: %version
Release: %release

Summary: Python implementation of Markdown text-to-HTML convertor.
Group: Development/Python
License: %gpl2plus | %bsd
Url: http://pypi.python.org/pypi/Markdown/2.1.1
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %modulename-%version.tar.bz2

BuildArch: noarch
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sun Feb 17 2008
BuildRequires: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

Conflicts: discount

%description
Markdown is a plain text formatting syntax designed to be as readable as
possible while being structured enough to allow conversion to other formats.

This package contains Python implementation of markdown-to-HTML convertor.

%if_with python3
%package -n python3-module-%modulename
Summary: Python 3 implementation of Markdown text-to-HTML convertor
Group: Development/Python

%description -n python3-module-%modulename
Markdown is a plain text formatting syntax designed to be as readable as
possible while being structured enough to allow conversion to other formats.
%endif

%package docs
Summary: Documentation for Markdown
Group: Development/Documentation
BuildArch: noarch

%description docs
Markdown is a plain text formatting syntax designed to be as readable as
possible while being structured enough to allow conversion to other formats.

This package contains documentation for Markdown.

%prep
%setup -n %modulename-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/%{modulename}_py \
	%buildroot%_bindir/%{modulename}_py3
%endif

%python_install --optimize=2

ln -s %{modulename}_py %buildroot%_bindir/%modulename

%files
%_bindir/*
%exclude %_bindir/%{modulename}_py3
%python_sitelibdir/*
# disable broken extension
#exclude %python_sitelibdir/%modulename/extensions/imagelinks.py*

%files docs
%doc docs

%if_with python3
%files -n python3-module-%modulename
%_bindir/%{modulename}_py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1
- Added module for Python 3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.3-alt2.1
- Rebuild with Python-2.7

* Fri Jul 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt2
- Added explicit conflict with discount

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1
- Version 2.0.3 (ALT #23510)

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6b-alt1.1
- Rebuilt with python 2.6

* Sun Feb 17 2008 Mikhail Gusarov <dottedmag@altlinux.org> 1.6b-alt1
- Initial build
