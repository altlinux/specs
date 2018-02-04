%def_with python3
%define mname sphinxcontrib
%define oname %mname-newsfeed

Name: python-module-%oname
Version: 0.1.4
Release: alt2.1
Summary: Sphinx extension for adding a simple Blog, News or Announcements

License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-newsfeed
Packager: Python Development Team <python at packages.altlinux.org>

Source: https://pypi.python.org/packages/2b/5e/8bc839b5c4ef030bf26eede24208a49f25d00033cbd4969b3895264f14db/%oname-%version.tar.gz
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif
BuildPreReq: python-devel python-module-setuptools
%py_provides %mname.newsfeed
%py_requires %mname

%description
%oname is a extension for adding a simple Blog, News or
Announcements section to a Sphinx website.
Features:
    Makes feed entries from Sphinx documents.
    Generates a list of entries with teasers.
    Saves the feed to a file in RSS format.
    Supports comments via Disqus.

You can see this extension in action at http://htsql.org/blog/. For more
examples, see demo directory in the source distribution.

%if_with python3
%package -n python3-module-%oname
Summary: Sphinx extension for adding a simple Blog, News or Announcements
Group: Development/Python
%py3_provides %mname.newsfeed
%py3_requires %mname

%description -n python3-module-%oname
%oname is a extension for adding a simple Blog, News or
Announcements section to a Sphinx website.
Features:
    Makes feed entries from Sphinx documents.
    Generates a list of entries with teasers.
    Saves the feed to a file in RSS format.
    Supports comments via Disqus.

You can see this extension in action at http://htsql.org/blog/. For more
examples, see demo directory in the source distribution.

Python 3 version.
%endif

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
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

%files
%doc LICENSE README
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*.pth
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.4-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 22 2017 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt2
- srpm build

* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt1
- Initial build for ALT Linux Sisyphus.
