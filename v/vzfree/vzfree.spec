Name: vzfree
Version: 0.1
Release: alt1

Summary: Checking Memory Usage inside OpenVZ VE

License: Public domain
Group: System/Configuration/Other
Url: http://hostingfu.com/article/vzfree-checking-memory-usage-inside-openvz-ve

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

%description
We all know that the Linux command free(1) is pretty useless inside an OpenVZ VE,
even those with meminfo virtualised.
So I basically wrote this little util to grab the data from the dreadful user_beancounters
and format them into something useful.

%prep
%setup -n %name-%version

%build
%make_build

%install
mkdir -p %buildroot%_bindir
%makeinstall PREFIX=%buildroot%_prefix

%files
%doc README
%_bindir/%name

%changelog
* Fri Apr 29 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
