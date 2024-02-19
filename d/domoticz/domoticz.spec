Name: domoticz
Version: 2023.2
Release: alt1

Summary: Open source Home Automation System

License: GPLv3+ and Apache-2.0 and Boost and BSD and MIT
Group: Other
Url: http://www.domoticz.com

# Source-url: https://github.com/domoticz/domoticz/archive/%version.tar.gz
Source: %name-%version.tar

Source1: %name.service
Source2: %name.conf
# Manually update version reported inside app
Source3: %name-appversion

# Use system tinyxpath (https://github.com/domoticz/domoticz/pull/1759)
Patch1: %name-tinyxpath.patch
# Fix python detection (https://github.com/domoticz/domoticz/pull/1749)
Patch2: %name-python.patch
# Python linking fix
Patch3: %name-python-link.patch

Patch4: %name-string.patch

AutoReq: yes, noperl, nolua
AutoProv: no

BuildRequires: boost-program_options-devel boost-signals-devel boost-asio-devel
BuildRequires: cereal-devel
BuildRequires: cmake
BuildRequires: curl-devel
BuildRequires: libfmt-devel
BuildRequires: fontpackages-devel
BuildRequires: gcc-c++
# TODO: remove
BuildRequires: git
BuildRequires: jsoncpp-devel
BuildRequires: libopenzwave-devel >= 1.6
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: liblua5-devel
#BuildRequires: minizip-compat-devel
BuildRequires: libminizip-devel
BuildRequires: libmosquitto-devel
BuildRequires: libssl-devel
BuildRequires: python3-devel
BuildRequires: libsqlite3-devel
BuildRequires: libudev-devel
#BuildRequires: tinyxpath-devel
BuildRequires: zlib-devel

Requires(pre):	shadow-utils
Requires(post):	udev-rules
Requires(postun):	udev-rules
Requires(preun):	udev-rules

#Requires: fonts-ttf-google-droid-all
#Recommends:	system-python-libs >= 3.4

%add_python3_lib_path %_datadir/%name
%add_python3_req_skip Domoticz DomoticzEvents DomoticzEx
%add_python3_req_skip bluepy

%description
Domoticz is a Home Automation System that lets you monitor and configure various
devices like: Lights, Switches, various sensors/meters like Temperature, Rain,
Wind, UV, Electra, Gas, Water and much more. Notifications/Alerts can be sent to
any mobile device

%prep
%setup
#patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Add support for future versions of Python by replacing hardcoded version with macro
%__subst 's/-lpythonVER/-lpython%__python3_version/' CMakeLists.txt
cp -p %SOURCE3 ./appversion.h

%build
%cmake \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DUSE_STATIC_LIBSTDCXX=NO \
 -DUSE_STATIC_OPENZWAVE=NO \
 -DUSE_OPENSSL_STATIC=NO \
 -DUSE_BUILTIN_JSONCPP=NO \
 -DUSE_BUILTIN_LIBFMT=NO \
 -DUSE_BUILTIN_LUA=NO \
 -DUSE_BUILTIN_MINIZIP=NO \
 -DUSE_BUILTIN_MQTT=NO \
 -DUSE_BUILTIN_SQLITE=NO \
 -DUSE_BUILTIN_TINYXPATH=NO \
 -DUSE_STATIC_BOOST=NO \
 -DCMAKE_INSTALL_PREFIX=%_datadir/%name \
 %nil
%cmake_build

%install
%cmake_install

# remove bundled OpenZWave configuration files so system files are used
rm -rv %buildroot%_datadir/%name/Config/

# remove docs, we grab them in files below
rm -v %buildroot%_datadir/%name/*.txt

# move binary to standard directory
mkdir -p %buildroot%_bindir/
mv %buildroot%_datadir/%name/%name %buildroot%_bindir/

# install systemd service and config
mkdir -p %buildroot%_sysconfdir/sysconfig/
mkdir -p %buildroot%_unitdir/
cp -p %SOURCE1 %buildroot%_unitdir/
cp -p %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

# create backups/database/plugins/scripts/ssl cert directory
mkdir -p %buildroot%_sharedstatedir/%name/{backups,plugins,scripts,templates}
mkdir -p %buildroot%_sharedstatedir/%name/scripts/{dzVents,lua,lua_parsers,python,templates}
mkdir -p %buildroot%_sharedstatedir/%name/scripts/dzVents/{data,generated_scripts,scripts}

# Disable the app's self-update script
chmod 644 %buildroot%_datadir/%name/updatedomo

# Unbundle DroidSans.ttf
#rm -f %buildroot%_datadir/%name/www/styles/elemental/fonts/DroidSans.ttf
#ln -s %_fontdir/google-droid/DroidSans.ttf \
#%buildroot%_datadir/%name/www/styles/elemental/fonts/
#rm -f %buildroot%_datadir/%name/www/styles/element-light/fonts/DroidSans.ttf
#ln -s %_fontdir/google-droid/DroidSans.ttf \
#%buildroot%_datadir/%name/www/styles/element-light/fonts/
#rm -f %buildroot%_datadir/%name/www/styles/element-dark/fonts/DroidSans.ttf
#ln -s %_fontdir/google-droid/DroidSans.ttf \
#%buildroot%_datadir/%name/www/styles/element-dark/fonts/

# Link default plugins and scripts to userdata directory
ln -s %_datadir/%name/scripts/dzVents/data/README.md \
%buildroot%_sharedstatedir/%name/scripts/dzVents/data/README.md
ln -s %_datadir/%name/scripts/dzVents/generated_scripts/README.md \
%buildroot%_sharedstatedir/%name/scripts/dzVents/generated_scripts/README.md
ln -s %_datadir/%name/scripts/dzVents/scripts/README.md \
%buildroot%_sharedstatedir/%name/scripts/dzVents/scripts/README.md
ln -s %_datadir/%name/scripts/templates/All.{dzVents,Lua,Python} \
%buildroot%_sharedstatedir/%name/scripts/templates/
ln -s %_datadir/%name/scripts/templates/Bare.dzVents \
%buildroot%_sharedstatedir/%name/scripts/templates/
ln -s %_datadir/%name/scripts/templates/Device.{dzVents,Lua} \
%buildroot%_sharedstatedir/%name/scripts/templates/
ln -s %_datadir/%name/scripts/templates/global_data.dzVents \
%buildroot%_sharedstatedir/%name/scripts/templates/
ln -s %_datadir/%name/scripts/templates/Group.dzVents \
%buildroot%_sharedstatedir/%name/scripts/templates/
ln -s %_datadir/%name/scripts/templates/HTTPRequest.dzVents \
%buildroot%_sharedstatedir/%name/scripts/templates/
ln -s %_datadir/%name/scripts/templates/Scene.dzVents \
%buildroot%_sharedstatedir/%name/scripts/templates/
ln -s %_datadir/%name/scripts/templates/Security.{dzVents,Lua} \
%buildroot%_sharedstatedir/%name/scripts/templates/
ln -s %_datadir/%name/scripts/templates/Time.Lua \
%buildroot%_sharedstatedir/%name/scripts/templates/
ln -s %_datadir/%name/scripts/templates/Timer.dzVents \
%buildroot%_sharedstatedir/%name/scripts/templates/
ln -s %_datadir/%name/scripts/templates/UserVariable.{dzVents,Lua} \
%buildroot%_sharedstatedir/%name/scripts/templates/

# Link web page templates to userdata directory
mv %buildroot%_datadir/%name/www/templates/{custom.example,readme.txt} \
%buildroot%_sharedstatedir/%name/templates
rm -rf %buildroot%_datadir/%name/www/templates
ln -s %_sharedstatedir/%name/templates \
%buildroot%_datadir/%name/www/templates


%pre
groupadd -f -r domoticz
useradd -r -g domoticz -d %_datadir/%name -s /sbin/nologin \
  -c "Domoticz Home Automation Server" domoticz || :
# For OpenZWave USB access (/dev/ttyACM#)
usermod -a -G dialout domoticz || :
usermod -a -G uucp domoticz || :

%post
%post_service %name

%preun
%preun_service %name

%files
%doc License.txt
%doc README.md History.txt
%_bindir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_datadir/%name/
%attr(0755,domoticz,domoticz) %_sharedstatedir/%name/
%_unitdir/%name.service

%changelog
* Sun Feb 18 2024 Vitaly Lipatov <lav@altlinux.ru> 2023.2-alt1
- initial build for ALT Sisyphus

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 2023.2-3
- Rebuilt for Boost 1.83

* Mon Dec 04 2023 Lukas Javorsky <ljavorsk@redhat.com> - 2023.2-2
- Rebuilt for minizip-ng transition Fedora change
- Fedora Change: https://fedoraproject.org/wiki/Changes/MinizipNGTransition

* Fri Nov 10 2023 Michael Cronenworth <mike@cchtml.com> - 2023.2-1
- New stable release

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 2022.1-10
- Rebuilt for Python 3.12

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.1-9
- Rebuilt due to fmt 10 update.

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2022.1-8
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2022.1-7
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Michael Cronenworth <mike@cchtml.com> - 2022.1-5
- Python 3.11 support (RHBZ#2093917)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2022.1-3
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2022.1-2
- Rebuilt for Boost 1.78

* Fri Mar 11 2022 Michael Cronenworth <mike@cchtml.com> - 2022.1-1
- New stable release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Michael Cronenworth <mike@cchtml.com> - 2021.1-9
- Handle templates directory upgrade path

* Mon Jan 03 2022 Michael Cronenworth <mike@cchtml.com> - 2021.1-8
- Symlink web page templates directory (RHBZ#1975094)

* Thu Dec 16 2021 Michael Cronenworth <mike@cchtml.com> - 2021.1-7
- Add patch for Python 3.10 support

* Wed Nov 03 2021 Björn Esser <besser82@fedoraproject.org> - 2021.1-6
- Rebuild (jsoncpp)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2021.1-5
- Rebuilt with OpenSSL 3.0.0

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 2021.1-4
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Richard Shaw <hobbes1069@gmail.com> - 2021.1-2
- Rebuild for new fmt version.

* Sat May 29 2021 Michael Cronenworth <mike@cchtml.com> - 2021.1-1
- New stable release

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 2020.2-9
- Rebuilt for removed libstdc++ symbols (#1937698)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2020.2-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2020.2-6
- Rebuilt for Boost 1.75

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Michael Cronenworth <mike@cchtml.com> - 2020.2-4
- Rebuild for Boost 1.73 (RHBZ#1843104)

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 2020.2-3
- Rebuild (jsoncpp)
- Add a patch to fix build with Python 3.9 (RHBZ#1842068)

* Mon Apr 27 2020 Michael Cronenworth <mike@cchtml.com> - 2020.2-2
- Link against older minizip

* Mon Apr 27 2020 Michael Cronenworth <mike@cchtml.com> - 2020.2-1
- New stable release

* Tue Apr 21 2020 Michael Cronenworth <mike@cchtml.com> - 2020.1-2
- Fix dzVents (RHBZ#1759558)

* Tue Mar 24 2020 Michael Cronenworth <mike@cchtml.com> - 2020.1-1
- New stable release

* Wed Feb 05 2020 Michael Cronenworth <mike@cchtml.com> - 4.11671-0.git20200202.1
- Update git checkout

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.11553-0.git20191207.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Michael Cronenworth <mike@cchtml.com> - 4.11553-0.git20191207.1
- Update git checkout (RHBZ#1780739)

* Wed Oct 09 2019 Michael Cronenworth <mike@cchtml.com> - 4.11352-0.git20191006.1
- Update git checkout and fix scripts directories (RHBZ#1759558)

* Sat Aug 31 2019 Michael Cronenworth <mike@cchtml.com> - 4.11250-0.git20190831.1
- Fix app version to match upstream versioning
- Fix default userdata location so the app can write to it

* Sat Aug 31 2019 Michael Cronenworth <mike@cchtml.com> - 4.10718-0.git20190831.1
- Version update to current master git checkout
- Compile against OpenZWave 1.6

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9700-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9700-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 4.9700-5
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 4.9700-4
- Append curdir to CMake invokation. (#1668512)

* Sun Nov 11 2018 Michael Cronenworth <mike@cchtml.com> - 4.9700-3
- Add patch to support Python 3.7

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9700-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Michael Cronenworth <mike@cchtml.com> - 4.9700-1
- Version update

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.8153-7
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Michael Cronenworth <mike@cchtml.com> - 3.8153-6
- Do not compile some of the extra Python files
- Add patch to fix bug in OZWCP javascript

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8153-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Michael Cronenworth <mike@cchtml.com> - 3.8153-4
- Add OpenZWave Command Class Barrier support
- Boost 1.66 support (RHBZ#1538585)

* Fri Sep 08 2017 Michael Cronenworth <mike@cchtml.com> - 3.8153-3
- Fix OpenZWave control panel symlink (RHBZ#1482266)
- Fix Python detection

* Mon Jul 31 2017 Michael Cronenworth <mike@cchtml.com> - 3.8153-2
- Fix OpenZWave control panel

* Mon Jul 31 2017 Michael Cronenworth <mike@cchtml.com> - 3.8153-1
- New upstream version
- Unbundle tinyxpath

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5877-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 3.5877-2
- Rebuilt for Boost 1.64

* Wed Jul 19 2017 Michael Cronenworth <mike@cchtml.com> - 3.5877-1
- Initial spec
