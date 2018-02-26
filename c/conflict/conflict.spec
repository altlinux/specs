%define date 20040901

Name: conflict
Version: 6.2
Release: alt1_%date

Summary: displays conflicting filenames in your execution path
License: BSD-style
Group: Text tools
Url: http://invisible-island.net/%name
Source: http://invisible-island.net/%name/%name.tar.gz

%description
CONFLICT examines the user-specifiable list of programs, looking for instances
in the user's path which conflict (i.e., the name appears in more than one
point in the path).

%prep
%setup -q -n %name-%date

%build
%configure
%make_build

%install
%makeinstall
%__install -d %buildroot%_man1dir/
%__mv %buildroot%_mandir/%name.* %buildroot%_man1dir/

%files
%_bindir/%name
%_man1dir/%name.*
%doc CHANGES COPYING README


%changelog
* Wed Feb 09 2005 Alex Murygin <murygin@altlinux.ru> 6.2-alt1_20040901
- new version

* Thu Aug 12 2004 Alex Murygin <murygin@altlinux.ru> 6.2-alt1_20040420
- Initial revision.

