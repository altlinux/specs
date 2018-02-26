Name: dxf2fig
Version: 2.13
Release: alt1

Summary: Autocad DXF to xfig convertor
License: GPL
Group: Development/Other
Url: http://ta.twi.tudelft.nl/ftp/dv/lemmens/

Packager: Igor Vlasenko <viy@altlinux.ru>
Source: http://ta.twi.tudelft.nl/ftp/dv/lemmens/%name-%version.tar.bz2


%description
Autocad DXF to xfig convertor utility.
   
%prep
%setup -q

%build
%make_build CFLAGS='%optflags -Wall -DVERSION=\"%version\" -DMODDATE=\"$(MODDATE)\"'

%install
%__install -D %{name} $RPM_BUILD_ROOT%_bindir/%{name}

%files
%doc Changelog README TODO
%_bindir/%{name}

%changelog
* Sat Nov 19 2005 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1
- initial build
