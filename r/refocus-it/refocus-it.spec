%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: refocus-it
Version: 2.0.0
Release: alt2

Summary: Tool to refocus images acquired by a defocused camera
License: GPLv2+
Group: Graphics

Url: http://refocus-it.sourceforge.net/
Source: http://dl.sf.net/refocus-it/refocus-it-%version.tar.gz

# Automatically added by buildreq on Mon Nov 26 2007
BuildRequires: libgimp-devel perl-XML-Parser

%description
Refocus-it is a tool, that can be used to refocus images acquired by a
defocused camera, blurred by gaussian or motion blur or any combination
of these.

%package -n gimp-plugin-%name
Group: Graphics
Summary: Gimp plugin to refocus images acquired by a defocused camera
Requires: gimp

Requires: %name = %version
# l10n (.po) file included in package with command-line utility but used
# also by plugin, hence this dependancy.

%description -n gimp-plugin-%name
Refocus-it is a plugin for GIMP, that can be used to refocus images
acquired by a defocused camera, blurred by gaussian or motion blur or
any combination of these.

%prep
%setup

%build
%configure --with-cmdline --with-gimp
%make_build

%install
%make_install install DESTDIR=%buildroot
%find_lang refocus-it

# In fact, only stub files installed, so get rid of them...
rm -rf %buildroot/usr/share/help

%files -f refocus-it.lang
%_bindir/*
%doc AUTHORS doc/{README,*.pgm}

%files -n gimp-plugin-%name
%gimpplugindir/plug-ins/*

%changelog
* Mon Nov 26 2007 Victor Forsyuk <force@altlinux.org> 2.0.0-alt2
- "Requires" for gimp was misplaced and put in standalone package, not
  gimp plugin.

* Fri Jun 01 2007 Victor Forsyuk <force@altlinux.org> 2.0.0-alt1
- Initial build.
