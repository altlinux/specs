Name: wireless-tools
Version: 29
Release: alt10
%define fullname wireless_tools.%version

Summary: Wireless ethernet configuration tools
Summary(ru_RU.UTF-8): Утилиты для настройки беспроводных сетей
Group: System/Kernel and hardware
License: GPL
Url: http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html
# http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/%fullname.tar.gz
Source0: %fullname.tar
Source1: iftab2rules
Patch1: wireless-tools-29-alt-makefile.patch
Patch2: wireless-tools-29-alt-ifrename-nowarn.patch

Requires: libwireless = %version-%release

%description
This package contain the Wireless tools, used to manipulate
the Wireless Extensions.  The Wireless Extension is an interface
allowing you to set Wireless LAN specific parameters and get the
specific stats for wireless networking equipment.

This is specifically useful since it allows manipulation of encryption
parameters possible with the GPL WaveLAN cards.

%description -l ru_RU.UTF-8
Этот пакет содержит набор программ, которые предназначены для настройки
и управления беспроводными сетевыми платами под Linux.

%package -n ifrename
Group: System/Kernel and hardware
Summary: %name tool renames network interfaces
Summary(ru_RU.UTF-8): утилита %name переименовывает сетевые интерфейсы
Requires: libwireless = %version-%release

%description -n ifrename
This package contains ifrename - a tool to rename network interfaces
considering different criterias consisting of: MAC address, link type,
module name, bus information, memory base address, irq line and wireless
protocol.  ifrename may be used by etcnet and udev packages, although
can be used standalone.

%description -n ifrename -l ru_RU.UTF-8
Этот пакет содержит ifrename.  Утилита предназначена для переименования
интерфейсов на основании критериев, которые включают MAC-адрес, канальный
тип интерфейса, имя модуля, расположение на системной шине, базовый адрес
разделяемой памяти, номер прерывания и беспроводный протокол.  Утилита
ifrename, в частности, может использоваться пакетами etcnet и udev, хотя
может быть использована и самостоятельно.

%package -n libwireless
Group: System/Libraries
Summary: Runtime library for %name

%description -n libwireless
This package contain runtime library for %name.

%package -n libwireless-devel
Group: Development/C
Summary: Development files for %name
Requires: libwireless = %version-%release
Obsoletes: %name-devel
Provides: %name-devel = %version-%release

%description -n libwireless-devel
This package contains development files for %name.

%prep
%setup -n %fullname
%patch1 -p1
%patch2 -p1

%build
make clean
make CFLAGS='%optflags -I.' IWLIBS='-L. -liw' BUILD_SHARED=1

%install
make install INSTALL_DIR=%buildroot/sbin \
	INSTALL_LIB=%buildroot%_libdir \
	INSTALL_INC=%buildroot%_includedir \
	INSTALL_MAN=%buildroot%_mandir

# Relocate shared library from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
	t=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
	[ -n "$t" ]
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

mkdir -p %buildroot%_sysconfdir
touch %buildroot%_sysconfdir/iftab

install -pDm755 %_sourcedir/iftab2rules \
	%buildroot/lib/ifrename/iftab2rules

%define convert_flag /var/run/ifrename-iftab2rules
%pre -n ifrename
rm -f %convert_flag
old_rules=/etc/udev/rules.d/19-udev-ifrename.rules
if [ $1 -ge 2 ] &&
   [ -s "$old_rules" ] &&
   grep -qs '^[[:space:]]*[^[:space:]#]' /etc/iftab; then
	if [ -x /lib/udev/write_net_rules ]; then
		touch %convert_flag
	else
		new_rules=/etc/udev/rules.d/70-persistent-net.rules
		cat >&2 <<EOF
WARNING: Old udev rules file $old_rules cannot be
converted to new udev rules file $new_rules,
udev persistent network rules is most likely to break after this update.
EOF
	fi
fi

%post -n ifrename
[ -f %convert_flag ] || exit 0
rm -f %convert_flag /etc/udev/rules.d/19-udev-ifrename.rules
exec /lib/ifrename/iftab2rules

%files
%doc INSTALL README DISTRIBUTIONS.txt
/sbin/*
%exclude /sbin/ifrename
%_mandir/man?/*
%exclude %_man8dir/ifrename*
%exclude %_man5dir/iftab*

%files -n ifrename
%config(noreplace,missingok) %verify(not md5 mtime size) %ghost %_sysconfdir/iftab
/sbin/ifrename
/lib/ifrename
%_man8dir/ifrename*
%_man5dir/iftab*

%files -n libwireless
/%_lib/*.so.*

%files -n libwireless-devel
%_libdir/*.so
%_includedir/*

%changelog
* Fri May 25 2012 Dmitry V. Levin <ldv@altlinux.org> 29-alt10
- ifrename: dropped udev-rule-generator requirement, added a warning
  to %%pre script for the rare case when old udev rules file still
  exists and cannot be converted (closes: #25820).

* Tue Dec 14 2010 Dmitry V. Levin <ldv@altlinux.org> 29-alt9
- Rebuilt for soname set-versions.

* Thu Jun 18 2009 Dmitry V. Levin <ldv@altlinux.org> 29-alt8
- ifrename: Do not require udev via iftab2rules script.

* Wed Jun 17 2009 Dmitry V. Levin <ldv@altlinux.org> 29-alt7
- ifrename:
  + Replaced udev-ifrename with udev-rule-generator.
  + Implemented automatic conversion from /etc/iftab to
    /etc/udev/rules.d/70-persistent-net.rules after update.

* Wed Jun 03 2009 Dmitry V. Levin <ldv@altlinux.org> 29-alt6
- udev-ifrename: Fixed comments handling (closes: #19313).

* Thu May 28 2009 Dmitry V. Levin <ldv@altlinux.org> 29-alt5
- Added udev-ifrename helper, updated udev rule
  (by Alexey Gladkov; closes: #19313).
- ifrename: Removed no longer needed configuration file locking
  introduced in previous build.

* Wed Mar 25 2009 Dmitry V. Levin <ldv@altlinux.org> 29-alt4
- ifrename: Obtain an exclusive lock on configuration file
  (Alexey Gladkov; closes: ALT#19313).

* Mon Feb 16 2009 Fr. Br. George <george@altlinux.ru> 29-alt3
- Add '-t' option to udev script

* Mon Oct 22 2007 Alexey Gladkov <legion@altlinux.ru> 29-alt2
- Fix ifrename rules for new udev.

* Sun Oct 14 2007 Alexey Gladkov <legion@altlinux.ru> 29-alt1
- New version 29.
- Add ifrename udev rule.
- Remove ifrename initscript.

* Wed Feb 21 2007 Alexey Gladkov <legion@altlinux.ru> 28-alt7.1
- NMU:
  + Add initscript for ifrename (#10885).
  + Spec cleanup.

* Tue Apr 11 2006 Alexei Takaseev <taf@altlinux.ru> 28-alt7
- Release 28
- Support WE20

* Sun Mar 19 2006 Alexei Takaseev <taf@altlinux.ru> 28-alt6.pre15
- 28-pre15
- fix shared linked
- fix build on x86_64

* Wed Dec 14 2005 Alexei Takaseev <taf@altlinux.ru> 28-alt6.pre10
- add patch to remove superfluous warnings

* Tue Oct 11 2005 Alexei Takaseev <taf@altlinux.ru> 28-alt5.pre10
- 28-pre10

* Thu Jan 20 2005 Alexei Takaseev <taf@altlinux.ru> 28-alt5.pre3
- Requires fixed on libwireless

* Sat Dec 11 2004 Alexei Takaseev <taf@altlinux.ru> 28-alt4.pre3
- fix ifrename man

* Wed Dec 08 2004 Alexei Takaseev <taf@altlinux.ru> 28-alt2.pre3
- wireless-tools splitted on several packages: wireless-tools,
  ifrename, libwireless and libwireless-devel

* Tue Dec 07 2004 Alexei Takaseev <taf@altlinux.ru> 28-alt1.pre3
- 28-pre3

* Fri Dec 03 2004 Alexei Takaseev <taf@altlinux.ru> 27-alt1
- new version

* Fri Apr 16 2004 Alexei Takaseev <taf@altlinux.ru> 26-alt3
- fix russian descriprion (#3940)

* Thu Mar 18 2004 Sergey V Turchin <zerg at altlinux dot org> 26-alt2.1.1
- add devel package

* Fri Mar 12 2004 Alexei Takaseev <taf@altlinux.ru> 26-alt2.1
- Use WE 16

* Tue Mar 09 2004 Alexei Takaseev <taf@altlinux.ru> 26-alt2
- Use WE 16

* Fri Aug 22 2003 Alexander Bokovoy <ab@altlinux.ru> 26-alt1
- new version
- Use WE 15 unless kernel will be updated

* Sun Oct 06 2002 Rider <rider@altlinux.ru> 25-alt1
- new version
- build shared libraries
- wireless tools moved to /sbin/

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 23-alt1
- new version (23)

* Sat Jan 05 2002 Rider <rider@altlinux.ru> 22-alt1
- new version

* Sat Mar 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 20-ipl3mdk
- Fixed build with glibc-2.2.2.

* Wed Jan 24 2001 Dmitry V. Levin <ldv@fandra.org> 20-ipl2mdk
- RE adaptions.

* Fri Jan 12 2001 Frederic Lepied <flepied@mandrakesoft.com> 20-2mdk
- moved from contrib

* Mon Dec 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 20-1mdk
- new in contribs
- used srpm from Kyle VanderBeek <kylev@yaga.com> 20-1mdk
	- First spec file for Mandrake distribution.

