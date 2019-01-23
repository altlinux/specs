%define  modulename pywikibot

Name:    python3-module-%modulename
Version: 3.0.20180710
Release: alt4

Summary: mediawiki bot library
License: MIT
Group:   Development/Python3
URL:     http://tools.wmflabs.org/pywikibot/core.tar.gz

Packager: Denis Medvedev <nbr@altlinux.org>


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3-module-requests
BuildRequires: python3-module-urllib3

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Pywikibot is a Python library and collection of scripts that
automate work on MediaWiki sites. Originally designed for Wikipedia,
it is now used throughout the Wikimedia Foundation's projects and on many other
wikis.

%prep
%setup -n %modulename-%version

%build
pushd core
%python3_build
popd

%install
pushd core
%python3_install
mkdir -p %buildroot/%_docdir/
cp *.rst generate_*.py pwb.py *.sample  *.txt %buildroot/%_docdir/
popd


%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%_docdir/*

%changelog
* Wed Jan 23 2019 Denis Medvedev <nbr@altlinux.org> 3.0.20180710-alt4
- Fixed build with corrected build instruction.

* Sun Oct 07 2018 Denis Medvedev <nbr@altlinux.org> 3.0.20180710-alt3
- Added forgotten main script pwv.py

* Sun Oct 07 2018 Denis Medvedev <nbr@altlinux.org> 3.0.20180710-alt2
- Added docs and scripts needed to run

* Sun Oct 07 2018 Denis Medvedev <nbr@altlinux.org> 3.0.20180710-alt1
Initial Sisyphus release
