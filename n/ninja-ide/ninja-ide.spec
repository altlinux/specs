Name:       ninja-ide
Version:    2.3
Release:    alt2
Summary:    Ninja IDE for Python development

Group:	    Development/Python
License:    GPLv3
URL:        http://www.ninja-ide.org/
Source0:    https://github.com/downloads/%{name}/%{name}/%{name}-%{version}.zip
# VCS:      https://github.com/ninja-ide/ninja-ide
Source1:    %{name}.desktop
Source2:    %{name}.1.gz

BuildRequires(pre): rpm-build-python
BuildRequires:  python-module-distribute
BuildRequires:  python-module-pyinotify
BuildRequires:  python-module-PyQt4-devel
BuildRequires:  unzip

BuildArch:      noarch

%description
NINJA-IDE (from the recursive acronym: "Ninja-IDE Is Not Just Another
IDE"), is a cross-platform integrated development environment (IDE).
NINJA-IDE runs on Linux/X11, Mac OS X and Windows desktop operating
systems, and allows developers to create applications for several
purposes using all the tools and utilities of NINJA-IDE, making the task
of writing software easier and more enjoyable.

%prep
%setup -q
# Remove Windows-specific part
rm -f ninja_ide/core/filesystem_notifications/windows.py

%build
%python_build

%install
%python_install

install -Dm 644 icon.png %buildroot/%_pixmapsdir/%{name}.png
install -Dm 644 %SOURCE1 %buildroot%_desktopdir/%{name}.desktop
install -Dm 644 %SOURCE2 %buildroot%_man1dir/%{name}.1.gz

find %buildroot -name 'pep8mod.py' | xargs chmod 0755

%files
%doc COPYING README.md
%_bindir/%name
%python_sitelibdir/ninja_ide/
%python_sitelibdir/ninja_tests/
%python_sitelibdir/NINJA_IDE-2.3-py2.7.egg-info/
%_pixmapsdir/%{name}.png
%_desktopdir/%{name}.desktop
%_man1dir/%{name}.1.*

%changelog
* Mon Dec 21 2015 Andrey Cherepanov <cas@altlinux.org> 2.3-alt2
- Do not use strict extension for man pages

* Thu Apr 17 2014 Andrey Cherepanov <cas@altlinux.org> 2.3-alt1
- Initial build for ALT Linux (based on Fedora spec)
