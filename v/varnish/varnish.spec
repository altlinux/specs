%def_disable static
Summary: Varnish is a high-performance HTTP accelerator
Name: varnish
Version: 2.1.5
Release: alt2
License: BSD-like
Group: System/Servers
Packager: Ilya Mashkin <oddity@altlinux.ru>
URL: http://www.varnish-cache.org/
Source0: http://downloads.sourceforge.net/varnish/varnish-%{version}.tar.gz
Source1: varnish.init
Source2: varnishlog.init
Requires: varnish-libs = %{version}-%{release}
Requires: logrotate
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

# Varnish actually needs gcc installed to work. It uses the C compiler 
# at runtime to compile the VCL configuration files. This is by design.
Requires: gcc

# Automatically added by buildreq on Fri Oct 03 2008
BuildRequires: gcc-c++ glibc-devel-static groff-base libncurses-devel tcl xsltproc
BuildRequires: libpcre-devel

%description
This is the Varnish high-performance HTTP accelerator. Documentation
wiki and additional information about Varnish is available on the following
web site: http://www.varnish-cache.org/

%package -n varnish-libs
Summary: Libraries for %{name}
Group: System/Libraries

%description -n varnish-libs
Libraries for %{name}.
Varnish is a high-performance HTTP accelerator.

%if_enabled static
%package -n devel-static
Summary: Static libraries for %{name}
Group: System/Libraries

%description -n devel-static
Static libraries for %{name}.
Varnish is a high-performance HTTP accelerator.
%endif # static

%prep
%setup

%build
%__subst 's/\[trunk\]/\[%{version}-%{release}\]/g' configure.ac
%__aclocal
%__libtoolize --copy --force
%__autoheader
%__automake --add-missing --copy --foreign
%__autoconf


%configure %{subst_enable static}

# We have to remove rpath - not allowed in Fedora
# (This problem only visible on 64 bit arches)
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%{__make} %{?_smp_mflags}

sed -e ' s/8080/80/g ' etc/default.vcl > redhat/default.vcl

%install
%brp_strip_none
%set_verify_elf_method textrel=relaxed,rpath=strict,unresolved=relaxed

make install DESTDIR=%{buildroot} INSTALL="install -p"

%if_disabled static
find %{buildroot}%{_libdir}/ -name '*.la' -exec rm -f {} ';'

find %{buildroot}%{_libdir}/ -name '*.so' -type l -exec rm -f {} ';'
%endif # statitc

mkdir -p %{buildroot}/var/lib/varnish
mkdir -p %{buildroot}%{_logdir}/varnish

%{__install} -D -m 0644 redhat/default.vcl %{buildroot}%{_sysconfdir}/varnish/default.vcl
%{__install} -D -m 0644 redhat/varnish.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/varnish
%{__install} -D -m 0644 redhat/varnish.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/varnish
%{__install} -D -m 0755 %SOURCE1 %{buildroot}%{_initdir}/varnish
%{__install} -D -m 0755 %SOURCE2 %{buildroot}%{_initdir}/varnishlog

%files
%{_libdir}/pkgconfig/varnishapi.pc
%{_sbindir}/*
%{_bindir}/*
%{_var}/lib/varnish
%{_logdir}/varnish
%{_includedir}/varnish/*.h
%{_man1dir}/*.1*
%{_man7dir}/*.7*
%doc INSTALL LICENSE README redhat/README.redhat redhat/default.vcl ChangeLog 
%dir %{_sysconfdir}/varnish/
%config(noreplace) %{_sysconfdir}/varnish/default.vcl
%config(noreplace) %{_sysconfdir}/sysconfig/varnish
%config(noreplace) %{_sysconfdir}/logrotate.d/varnish
%config(noreplace) %{_initdir}/varnish
%config(noreplace) %{_initdir}/varnishlog

%files -n varnish-libs
%{_libdir}/*.so.*
%doc LICENSE

%if_enabled static
%files -n devel-static
%{_libdir}/*.so
%{libdir}/*.la
%endif # static

%post
%post_service varnish
%post_service varnishlog

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -n -g %name -d %_var/run/%name \
 -s /dev/null -c 'Varnish HTTP accelerator' %name 2>/dev/null ||:

%preun
%preun_service varnish
%preun_service varnishlog

%changelog
* Fri Dec 30 2011 Ilya Mashkin <oddity@altlinux.ru> 2.1.5-alt2
- fix build

* Sun Feb 20 2011 Ilya Mashkin <oddity@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Wed Dec 01 2010 Ilya Mashkin <oddity@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.0-alt1.beta2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for varnish-libs
  * postun_ldconfig for varnish-libs
  * postclean-05-filetriggers for spec file

* Fri Oct 03 2008 Sergey Ivanov <seriv@altlinux.ru> 2.0-alt1.beta2
- 2.0-alt1.beta2

* Wed Jul 04 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.4.3-alt3
- fixed to match ALTLinux standards, thanks to Slava Semushin

* Tue Jul 03 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.4.3-alt2
- restructured for building with gear

* Sun Jun 17 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.4.3-alt1
- updated build to 1.0.4-3 tag

* Thu Jun 14 2007 Sergey Ivanov <seriv@altlinux.ru> 1.0.4-alt1
- initial build for Sisyphus

* Fri May 18 2007 Dag-Erling Smørgrav <des@des.no> - 1.0.4-1
- Bump Version and Release for 1.0.4

* Wed May 16 2007 Ingvar Hagelund <ingvar@linpro.no> - 1.0.svn-20070517
- Wrapping up for 1.0.4
- Changes in sysconfig and init scripts. Syncing with files in
  trunk/debian

* Fri May 11 2007 Ingvar Hagelund <ingvar@linpro.no> - 1.0.svn-20070511
- Threw latest changes into svn trunk
- Removed the conversion of manpages into utf8. They are all utf8 in trunk

* Wed May 09 2007 Ingvar Hagelund <ingvar@linpro.no> - 1.0.3-7
- Simplified the references to the subpackage names
- Added init and logrotate scripts for varnishlog

* Mon Apr 23 2007 Ingvar Hagelund <ingvar@linpro.no> - 1.0.3-6
- Removed unnecessary macro lib_name
- Fixed inconsistently use of brackets in macros
- Added a condrestart to the initscript
- All manfiles included, not just the compressed ones
- Removed explicit requirement for ncurses. rpmbuild figures out the 
  correct deps by itself.
- Added ulimit value to initskript and sysconfig file
- Many thanks to Matthias Saou for valuable input

* Mon Apr 16 2007 Ingvar Hagelund <ingvar@linpro.no> - 1.0.3-5
- Added the dist tag
- Exchanged  RPM_BUILD_ROOT variable for buildroot macro
- Removed stripping of binaries to create a meaningful debug package
- Removed BuildRoot and URL from subpackages, they are picked from the
  main package
- Removed duplication of documentation files in the subpackages
- 'chkconfig --list' removed from post script
- Package now includes _sysconfdir/varnish/
- Trimmed package information
- Removed static libs and .so-symlinks. They can be added to a -devel package
  later if anybody misses them

* Wed Feb 28 2007 Ingvar Hagelund <ingvar@linpro.no> - 1.0.3-4
- More small specfile fixes for Fedora Extras Package
  Review Request, see bugzilla ticket 230275
- Removed rpath (only visible on x86_64 and probably ppc64)

* Tue Feb 27 2007 Ingvar Hagelund <ingvar@linpro.no> - 1.0.3-3
- Made post-1.0.3 changes into a patch to the upstream tarball
- First Fedora Extras Package Review Request

* Fri Feb 23 2007 Ingvar Hagelund <ingvar@linpro.no> - 1.0.3-2
- A few other small changes to make rpmlint happy

* Thu Feb 22 2007 Ingvar Hagelund <ingvar@linpro.no> - 1.0.3-1
- New release 1.0.3. See the general ChangeLog
- Splitted the package into varnish, libs and
  libs-devel

* Thu Oct 19 2006 Ingvar Hagelund <ingvar@linpro.no> - 1.0.2-7
- Added a Vendor tag

* Thu Oct 19 2006 Ingvar Hagelund <ingvar@linpro.no> - 1.0.2-6
- Added redhat subdir to svn
- Removed default vcl config file. Used the new upstream variant instead.
- Based build on svn. Running autogen.sh as start of build. Also added
  libtool, autoconf and automake to BuildRequires.
- Removed rule to move varnishd to sbin. This is now fixed in upstream
- Changed the sysconfig script to include a lot more nice features.
  Most of these were ripped from the Debian package. Updated initscript
  to reflect this.

* Tue Oct 10 2006 Ingvar Hagelund <ingvar@linpro.no> - 1.0.1-3
- Moved Red Hat specific files to its own subdirectory

* Tue Sep 26 2006 Ingvar Hagelund <ingvar@linpro.no> - 1.0.1-2
- Added gcc requirement.
- Changed to an even simpler example vcl in to /etc/varnish (thanks, perbu)
- Added a sysconfig entry

* Fri Sep 22 2006 Ingvar Hagelund <ingvar@linpro.no> - 1.0.1-1
- Initial build.
