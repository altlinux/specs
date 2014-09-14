%define oname check_pgactivity
Name: nagios-plugins-check_pgactivity
Version: 1.13
Release: alt1

Summary: Nagios(R) plug-in for checking PostgreSQL status
License: BSD like
Group: Monitoring

Url: https://github.com/OPMDG/check_pgactivity

Source: %name-%version.tar

BuildArchitectures: noarch

Requires: nagios-nrpe

# nagios uses /usr/lib for plugins in any arch
%define pluginsdir %_prefix/lib/nagios/plugins

# manually removed:  rpm-build-python3 ruby ruby-stdlibs
# Automatically added by buildreq on Sun Sep 14 2014 (-bi)
# optimized out: perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage python-base python3 python3-base
BuildRequires: perl-podlators

%description
Nagios plug-in check_pgactivity is the part of Open PostgreSQL Monitoring (OPM) project.

%prep
%setup

%install
mkdir -p %buildroot%pluginsdir/
install -m755 %oname %buildroot%pluginsdir/

%files
%pluginsdir/%oname

%changelog
* Sun Sep 14 2014 Vitaly Lipatov <lav@altlinux.ru> 1.13-alt1
- initial build for ALT Linux Sisyphus
