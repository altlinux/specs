Name: zsh-syntax-highlighting
Version: 0.7.1
Release: alt1

Summary: Fish shell like syntax highlighting for Zsh
License: BSD
Url: https://github.com/zsh-users/zsh-syntax-highlighting
Group: Shells
Source0: %version.tar.gz

BuildArch: noarch

BuildRequires: zsh

Requires: zsh

%description
This package provides syntax highlighting for the shell zsh. It enables
highlighting of commands whilst they are typed at a zsh prompt into an
interactive terminal. This helps in reviewing commands before running them,
particularly in catching syntax errors.

%prep
%setup
cat > syntax-highlighting.zsh <<@@@
source %_datadir/zsh/syntax-highlighting/zsh-syntax-highlighting.zsh
@@@

%build
make

%install
make install DESTDIR=%buildroot PREFIX=%prefix SHARE_DIR=%buildroot/%_datadir/zsh/syntax-highlighting

install -D syntax-highlighting.zsh %buildroot/%_sysconfdir/zshrc.d/syntax-highlighting.zsh

%check
%make test
#make perf

%files
%doc %_defaultdocdir/%name
%_datadir/zsh/syntax-highlighting
%_sysconfdir/zshrc.d/syntax-highlighting.zsh

%changelog
* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 0.7.1-alt1
- Autobuild version bump to 0.7.1

* Thu Nov 15 2018 Fr. Br. George <george@altlinux.ru> 0.6.0-alt1
- Initial build from Fedora

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 02 2017 Michael Kuhn <suraia@ikkoku.de> - 0.6.0-1
- Update to 0.6.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 29 2016 Michael Kuhn <suraia@ikkoku.de> - 0.5.0-1
- Update to 0.5.0

* Mon Aug 29 2016 Michael Kuhn <suraia@ikkoku.de> - 0.4.1-1
- Initial package
