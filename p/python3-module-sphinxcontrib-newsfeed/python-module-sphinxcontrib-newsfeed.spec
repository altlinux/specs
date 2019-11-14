%define mname sphinxcontrib
%define oname %mname-newsfeed

Name: python3-module-%oname
Version: 0.1.4
Release: alt3

Summary: Sphinx extension for adding a simple Blog, News or Announcements
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinxcontrib-newsfeed
BuildArch: noarch

Source: https://pypi.python.org/packages/2b/5e/8bc839b5c4ef030bf26eede24208a49f25d00033cbd4969b3895264f14db/%oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %mname.newsfeed
%py3_requires %mname


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

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*.pth


%changelog
* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.4-alt3
- python2 disabled

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.4-alt2.2
- (NMU) rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.4-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 22 2017 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt2
- srpm build

* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 0.1.4-alt1
- Initial build for ALT Linux Sisyphus.
