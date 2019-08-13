Name: emacs-dash
Version: 2.16.0
Release: alt1

Summary: A modern list library for Emacs

License: GPL-3.0-or-later
Group: Editors
Url: https://github.com/magnars/dash.el

# repacked https://github.com/magnars/dash.el/archive/%version.tar.gz
Source: %version.tar

BuildRequires: emacs-nox
BuildRequires: make
Requires: emacs

BuildArch: noarch

%description
Dash is a modern list API for Emacs that requires no "cl".

%prep
%setup -n dash.el-%version

%build
emacs -L . --batch -f batch-byte-compile *.el

%check
./run-tests.sh

%install
install -d %buildroot%_emacslispdir
install -m 644 *.el *.elc %buildroot%_emacslispdir

%files
%doc README.md
%_emacslispdir/dash*.el
%_emacslispdir/dash*.elc

%changelog
* Sat Aug 03 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.16.0-alt1
- Initial build for ALT Sisyphus based on openSUSE spec.
