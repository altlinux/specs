Name: nano-editor
Version: 0.1
Release: alt1%ubt

Group: System/Configuration/Other
Summary: Set EDITOR environment variable to nano by default
License: GPL

BuildArch: noarch

Requires: nano

Source: nano-editor.sh

# Automatically added by buildreq on Wed Jul 26 2017 (-bi)
# optimized out: python-base python-modules python3 python3-base rpm-build-python3
#BuildRequires: python-module-google python3-dev python3-module-zope ruby ruby-stdlibs
BuildRequires(pre): rpm-build-ubt

%description
Set EDITOR environment variable to nano by default

%prep

%install
install -D -m 0755 %SOURCE0 %buildroot/%_sysconfdir/profile.d/nano-editor.sh

%files
%config(noreplace) %_sysconfdir/profile.d/nano-editor.sh

%changelog
* Wed Jul 26 2017 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1%ubt
- initial build
