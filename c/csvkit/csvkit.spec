%def_with doc
Name:    csvkit
Version: 2.0.1
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

%description
%summary.

%prep
%setup -n %name-%version

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
* Tue Jul 16 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.0.1-alt1
- New version 2.0.1.

* Mon May 27 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.0.0-alt1
- New version 2.0.0.

* Mon Apr 24 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.1-alt1
- New version 1.1.1.

* Wed Feb 07 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
