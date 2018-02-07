%def_with doc
Name:    csvkit
Version: 1.0.2
Release: alt1

Summary: A suite of utilities for converting to and working with CSV, the king of tabular file formats
License: MIT
Group:   Other
URL:     https://github.com/wireservice/csvkit

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
%{?_with_doc:BuildRequires: python3-module-sphinx-sphinx-build-symlink}

BuildArch: noarch

Source:  %name-%version.tar
Patch0: csvkit-1.0.2-alt-disable-import-sphinx_rtd_them.patch

%description
%summary.

%prep
%setup -n %name-%version
%patch0 -p1

%build
%python3_build

%if_with doc
cd docs
make man text
cd -
%endif

%install
%python3_install

%if_with doc
mkdir -p %buildroot%_man1dir
cp docs/_build/man/*.1 %buildroot%_man1dir
%endif

%files
%_bindir/csvclean
%_bindir/csvformat
%_bindir/csvjoin
%_bindir/csvlook
%_bindir/csvsort
%_bindir/csvstack
%_bindir/in2csv
%_bindir/sql2csv
%_bindir/csvstat
%_bindir/csvsql
%_bindir/csvpy
%_bindir/csvjson
%_bindir/csvgrep
%_bindir/csvcut
%if_with doc
%doc %_man1dir/*
%doc docs/_build/text/*
%endif
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Wed Feb 07 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
