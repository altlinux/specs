Name: apache2-mod_mpm_itk
Summary: MPM Itk for Apache HTTP Server
Version: 2.4.7
Release: alt1
URL: http://mpm-itk.sesse.net/
License: ASL 2.0
Group: System/Servers
Packager: Sergey Alembekov <rt@altlinux.ru>

Source: http://mpm-itk.sesse.net/mpm-itk-%{version}.tar.gz
SOURCE1: README.alt

BuildRequires: apache2-devel 

Obsoletes: apache2-httpd-itk

%description
This package contain mpm-itk which is an MPM (Multi-Processing Module)
for the Apache web server. Mpm-itk allows you to run each of your vhost
under a separate uid and gid - in short, the scripts and configuration
files for one vhost no longer have to be readable for all the other
vhosts.

In summary it is Apache module (opposite CGI solutions like suexec),
fast and allow safely use non-thread-aware code software (like many PHP
extensions f.e.)

%prep
%setup -q -n mpm-itk-%version

%build
export APXS=%apache2_apxs
%configure
%make
install %SOURCE1 README.alt

%install
install -D .libs/mpm_itk.so %{buildroot}/%apache2_moduledir/mod_mpm_itk.so
install -d %{buildroot}%apache2_mods_available

cat > %{buildroot}/%apache2_mods_available/mpm_itk.load << EOF
LoadModule mpm_itk_module %apache2_moduledir/mod_mpm_itk.so
EOF


%files
%doc README CHANGES README.alt
%apache2_libexecdir/mod_mpm_itk.so
%config(noreplace) %apache2_mods_available/mpm_itk.load

%changelog
* Thu Apr 28 2016 Sergey Alembekov <rt@altlinux.ru> 2.4.7-alt1
- initial build
