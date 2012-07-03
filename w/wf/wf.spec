Name: wf
Version: 0.41
Release: alt1

Summary: Simple word frequency counter
License: GPL2
Group: Text tools
Url: http://www.async.com.br/~marcelo/wf/
Source: %name-%version.tar
Packager: Evgenii Terechkov <evg@altlinux.org>

%description
wf scans a text file and counts the frequency of words through the whole text

%prep
%setup

%build
%autoreconf
%configure
make

%install
%makeinstall

%files
%_bindir/%name
%_man1dir/%name.*

%doc AUTHORS NEWS README TODO ChangeLog

%changelog
* Sun Mar 29 2009 Terechkov Evgenii <evg@altlinux.ru> 0.41-alt1
- Initial build for ALT Linux Sisyphus
