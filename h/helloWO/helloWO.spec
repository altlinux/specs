Name:		helloWO
Version:	5.4.3
Release:	alt3
Summary:	WebObjects starter-application "HelloWOrld"  with complete WebObjects libraries set
Summary(ru_RU.UTF-8): стартовое WebObjects-приложение "HelloWOrld" с полным набором библиотек WebObjects

License:	Distributable
Group:		Networking/WWW
#Vendor:		Apple Inc.
URL:		http://support.apple.com/kb/DL688
BuildArch: 	noarch

Packager:  	Gennady Kushnir <baywind@altlinux.org>, Andrey Cherepanov <cas@altlinux.org>

Source:		%{name}-%{version}.tar

Provides:	hellowo = 5.4.3
BuildRequires:	rpm-macros-webobjects
Requires: 	java >= 1.5
AutoReq:	noshell noshebang

%description
HelloWOrld starter application with complete WebObjects libraries set.

WebObjects is a set java frameworks for building complex web-applications.
It gives developers a comprehensive suite of tools and frameworks for quickly 
developing standards-based web services and Java server applications. 
A powerful rapid application development environment, backed by web service,
data access, and page generation capabilities, extends the reach of developers
and reduces the cost of ownership by ensuring flexible, maintainable design.
WebObjects is the ideal way to develop, deploy, and extend powerful web services.

%description -l ru_RU.UTF-8
стартовое приложение HelloWOrld с полным набором необходимых библиотек WebObjects.
WebObjects - набор Java-библиотек для разработки сложных Web-приложений

%prep
%setup
rm -rf Library/WebObjects/Adaptors
rm -rf Local/Library/WebObjects/Configuration
rm -rf Local/Library/WebObjects/Logs

%build

%pre
# create users for WebObjects application Server
if [ "$1" = 1 ] ; then 
   %_sbindir/groupadd %wo_group ||:
   %_sbindir/useradd -g %wo_group -r %wo_user ||:
fi

%install
mkdir -p %buildroot%wo_next_root
cp -r Local %buildroot%wo_next_root/
cp -r Library %buildroot%wo_next_root/
mkdir -p %buildroot%_sysconfdir/profile.d/
mkdir -p %buildroot%wo_configdir
mkdir -p %buildroot%wo_logdir

# add $NEXT_ROOT definition to system initialisation
echo "export NEXT_ROOT=\"%wo_next_root\"" > %buildroot%_sysconfdir/profile.d/webobjects.sh

mkdir -p %buildroot%wo_web_resources/Frameworks/
mkdir -p %buildroot%wo_frameworks

%post
ln -s %wo_configdir %wo_localroot/Library/WebObjects/Configuration
ln -s %wo_logdir %wo_localroot/Library/WebObjects/Logs

cd %wo_woroot/Library/Frameworks/

for f in *.framework; do
  if [ -d $f/WebServerResources ] ; then
    mkdir -p %wo_web_resources/Frameworks/$f
    ln -fns %wo_woroot/Library/Frameworks/$f/WebServerResources/ %wo_web_resources/Frameworks/$f/
  fi
done

%preun
if [ "$1" = 0 ] ; then
  cd %wo_woroot/Library/Frameworks/

  for f in *.framework; do
    if [ -d %wo_web_resources/Frameworks/$f ] ; then
      rm -rf o_web_resources/Frameworks/$f
    fi
  done
fi

%postun

if [ "$1" = 0 ] ; then 
   %_sbindir/groupdel %wo_group ||:
   %_sbindir/userdel -r %wo_user ||:
fi

%files
%attr(0755,root,root) %_sysconfdir/profile.d/webobjects.sh
%defattr(-,%wo_user,%wo_group)
%wo_next_root
%attr(0750,%wo_user,%wo_group) %wo_woroot/Library/WebObjects/JavaApplications/wotaskd.woa/Contents/Resources/SpawnOfWotaskd.sh
%dir %config(noreplace) %wo_configdir
%dir %wo_logdir

%changelog
* Sun Nov 21 2010 Gennady Kushnir <baywind@altlinux.org> 5.4.3-alt3
- replaced russian words in HelloWOrld.woa with english
- removed unused system WO applications
* Thu Oct 07 2010 Gennady Kushnir <baywind@altlinux.org> 5.4.3-alt2
- ignoring errors creating and deleting user and group in %%pre and %%postun scripts
- commented out Vendor tag
* Wed Sep 15 2010 Gennady Kushnir <baywind@altlinux.org> 5.4.3-alt1
- Initial release
