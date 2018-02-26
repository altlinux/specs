
Name: elyxer
Version: 1.2.3
Release: alt1

Summary: eLyXer (pronounced elixir) is a LyX to HTML converter.
License: GPLv3
Group: Development/Python

Url: http://elyxer.nongnu.org
Packager: Damir Shayhutdinov <damir@altlinux.ru>
BuildArch: noarch

Source: http://download.savannah.gnu.org/releases/elyxer/%name-%version.tar.gz
Source1: elyxer.1
Source2: loremipsumize.1

BuildPreReq: %py_dependencies setuptools

%description
eLyXer is a standalone tool: it does not require that LyX is installed
to run. It can convert documents generated with versions of LyX
from 1.5.5 through 2.0 (and probably earlier versions) to HTML or XHTML

%prep
%setup

%build
touch src/elyxer/conf/config.py
./make
cp src/setup.py setup.py
%python_build

%install
%python_install
mkdir -p %buildroot%_datadir %buildroot%_man1dir
cp -r po/locale %buildroot%_datadir/
cp %SOURCE1 %SOURCE2 %buildroot%_man1dir/

for i in %buildroot%_bindir/*.py; do
	ln -s `basename $i` %buildroot/%_bindir/`basename $i .py`
done

%find_lang %name
%files -f %name.lang
%_bindir/*
%_man1dir/*
%doc docs
%exclude %python_sitelibdir

%changelog
* Tue Dec 13 2011 Damir Shayhutdinov <damir@altlinux.ru> 1.2.3-alt1
- Initial build for ALT Linux

