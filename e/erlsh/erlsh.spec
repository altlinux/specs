Name: erlsh
Version: 0.1.1
Release: alt1
Summary: Erlang shell with readline
License: %pubdomain
Group: Shells
URL: http://git.altlinux.org/people/led/packages/%name.git
Source: %name.sh.in
BuildArch: noarch
Requires: rlwrap erlang
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses rpm-macros-erlang

%description
Erlang shell with readline.


%prep
install -m 0644 %SOURCE0 ./%name.sh.in


%build
sed 's|@ERL@|%__erlang|g' %name.sh.in > %name.sh


%install
install -D -m 0755 %name.sh %buildroot%_bindir/%name


%files
%_bindir/*


%changelog
* Fri May 08 2009 Led <led@altlinux.ru> 0.1.1-alt1
- 0.1.1:
  + fixed typo
- added URL

* Thu Apr 30 2009 Led <led@altlinux.ru> 0.1-alt1
- initial build
