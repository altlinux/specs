Name: fw-template-erlang
Version: 0.1.37
Release: alt2
Summary: Erlang template for framewerk
License: %gpl2plus
Group: Development/Erlang
URL: http://fwtemplates.googlecode.com
Source: %url/files/%name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch
Requires: framewerk
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses

%description
Erlang template for framewerk. Features:
 - automatic generation of OTP compliant application file via scanning
   source
 - convenient eunit and cover integration
 - edoc integration


%prep
%setup
%patch -p1


%build
%configure
%make_build


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS ChangeLog README TODO
%_datadir/fw/m4/*
%_datadir/fw/template/*
%_libexecdir/fw/*


%changelog
* Mon Mar 02 2009 Led <led@altlinux.ru> 0.1.37-alt2
- default +debug_info replaced with $(ERLC_FLAGS)

* Sun Mar 01 2009 Led <led@altlinux.ru> 0.1.37-alt1
- initial build
