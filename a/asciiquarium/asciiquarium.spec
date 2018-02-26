Name: asciiquarium
Version: 1.0
Release: alt1

Summary: Aquarium/sea animation in ASCII art
License: GPL
Group: Toys
Url: http://www.robobunny.com/projects/asciiquarium/

Source: %url/%{name}_%version.tar.gz

BuildArch: noarch

BuildPreReq: perl-Curses perl-Term-Animation

%description
Asciiquarium is an aquarium/sea animation in ASCII art.

%prep
%setup -n %{name}_%version

%install
%__mkdir_p %buildroot%_bindir
%__install -p -m755 %name %buildroot%_bindir

%files
%_bindir/*
%doc CHANGES README

%changelog
* Mon Sep 19 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.0-alt1
- initial build
