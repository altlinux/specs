%define ast_version %{get_version asterisk1.6.2-devel}
%define modules_dir %_libdir/asterisk/%ast_version/modules

Name: asterisk1.6.2-chan_dongle
Summary: Channel driver for Asterisk to use Huawei 3G modem series.
Version: 1.1
Release: alt4
License: GPL
Group: System/Libraries

Source: %name-%version.tar

# Automatically added by buildreq on Sat Oct 03 2009
BuildRequires(pre): asterisk1.6.2-devel

Requires: usb_modeswitch
Requires: asterisk1.6.2 = %ast_version

%description
%summary

%prep
%setup

%build
export CFLAGS="-I /usr/include/asterisk-%ast_version" 

%configure \
    --with-asterisk=/usr/include/asterisk-%ast_version
%make_build OPTFLAGS="-I /usr/include/asterisk-%ast_version" LIBS="-l pthread"

%install
mkdir -p %buildroot%modules_dir/
cp *.so %buildroot%modules_dir/
mkdir -p %buildroot%_docdir/%name

%files
%modules_dir/*.so
%doc LICENSE.txt README.txt TODO.txt INSTALL BUGS etc

%changelog
* Mon Jan 02 2012 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt4
- Asterisk update

* Fri Jul 15 2011 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt3
- Asterisk update

* Sat Jun 25 2011 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt1.r2
- first build for Sisyphus

