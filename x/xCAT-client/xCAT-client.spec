Name: xCAT-client
Summary: Core executables and data of the xCAT management project
Version: 2.5.1
Release: alt0.4
License: EPL
Group: System/Servers
Source: xCAT-client-%{version}.tar
Source1: xcat.sh
Source2: xcat.csh
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildArch: noarch

# fping or nmap is needed by pping (in case xCAT-client is installed by itself on a remote client)
Requires: nmap
Requires: expat
Requires: openslp
BuildRequires: perl-xCAT perl-IO-Socket-SSL
BuildRequires: perl-podlators

%description
xCAT-client provides the xCAT commands (chtab, chnode, rpower, etc)
helpflul in administrating systems at scale, with particular attention
paid to large HPC clusters.

# RVID - remote video (VGA) depends from JAVA Runtime Environment
%add_findreq_skiplist %{_datadir}/xcat/rvid/rvid.imm
%add_findreq_skiplist %{_datadir}/xcat/rvid/rvid.blade

%prep
%setup -q

%build
# Convert pods to man pages and html pages
./xpod2man

%install

# Binaries.
install -d -pm 755 %{buildroot}%{_bindir}
install -d -pm 755 %{buildroot}%{_sbindir}

install -D -pm 755 bin/* %{buildroot}%{_bindir}
install -D -pm 755 sbin/* %{buildroot}%{_sbindir}

# Manpages.
install -d -pm 755 %{buildroot}%{_man1dir}
install -d -pm 755 %{buildroot}%{_man3dir}
install -d -pm 755 %{buildroot}%{_man5dir}
install -d -pm 755 %{buildroot}%{_man8dir}

install -D -pm 644 share/man/man1/* %{buildroot}%{_man1dir}
install -D -pm 644 share/man/man3/* %{buildroot}%{_man3dir}
install -D -pm 644 share/man/man5/* %{buildroot}%{_man5dir}
install -D -pm 644 share/man/man8/* %{buildroot}%{_man8dir}

# Other
install -d -pm 755 %{buildroot}%{_datadir}/xcat/{tools,rvid}
install -D -pm 755 share/xcat/rvid/* %{buildroot}%{_datadir}/xcat/rvid
install -D -pm 755 share/xcat/tools/* %{buildroot}%{_datadir}/xcat/tools

ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rpower
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rscan
ln -sf ../bin/xcatclient %{buildroot}%{_sbindir}/makedhcp
ln -sf ../bin/xcatclient %{buildroot}%{_sbindir}/makehosts
ln -sf ../bin/xcatclient %{buildroot}%{_sbindir}/makeknownhosts
ln -sf ../bin/xcatclient %{buildroot}%{_sbindir}/nodeset
ln -sf ../bin/xcatclient %{buildroot}%{_sbindir}/setupiscsidev
ln -sf ../bin/xcatclient %{buildroot}%{_sbindir}/makeconservercf
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rbeacon
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rvitals
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/nodestat
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rinv
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rflash
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rspreset
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rsetboot
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rbootseq
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/reventlog
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/nodels
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/nodech
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/noderm
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rnetboot
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/getmacs
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/mkvm
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rmvm
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/lsvm
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/chvm
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/tabgrep
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/renergy
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/litetree
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/litefile
# Don't pack tools designed to work with IBM blades
#ln -sf ../bin/xcatclient %{buildroot}/%{_bindir}/lsflexnode
#ln -sf ../bin/xcatclient %{buildroot}/%{_bindir}/rmflexnode
#ln -sf ../bin/xcatclient %{buildroot}/%{_bindir}/mkflexnode
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rmhypervisor
ln -sf ../bin/xcatclient %{buildroot}%{_sbindir}/makedns
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/lsslp
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/nodegrpch
ln -sf ../bin/xcatclientnnr %{buildroot}%{_sbindir}/tabdump
ln -sf ../bin/xcatclientnnr %{buildroot}%{_sbindir}/packimage
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/gettab
ln -sf ../bin/xcatclientnnr %{buildroot}%{_sbindir}/nodeadd
ln -sf ../bin/xcatclientnnr %{buildroot}%{_sbindir}/tabprune
ln -sf ../bin/xcatclientnnr %{buildroot}%{_sbindir}/makenetworks
ln -sf ../bin/xcatclientnnr %{buildroot}%{_sbindir}/copycds
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/regnotif
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/unregnotif
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/monstart
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/monstop
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/monls
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/moncfg
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/mondecfg
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/monadd
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/monrm
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/monshow
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/sinv
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/rollupdate
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/runrollupdate
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/webrun
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/ilitefile
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/liteimg
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/gennr
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/imgexport
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/imgimport
ln -sf ../bin/xcatclientnnr %{buildroot}%{_bindir}/lsxcatd
ln -sf ../bin/xcatclientnnr %{buildroot}%{_sbindir}/makeroutes
ln -sf ../bin/xcatclientnnr %{buildroot}%{_sbindir}/snmove
ln -sf ../bin/xcatDBcmds %{buildroot}%{_bindir}/mkdsklsnode
ln -sf ../bin/xcatDBcmds %{buildroot}%{_bindir}/rmdsklsnode
ln -sf ../bin/xcatDBcmds %{buildroot}%{_bindir}/mknimimage
ln -sf ../bin/xcatDBcmds %{buildroot}%{_bindir}/chkosimage
ln -sf ../bin/xcatDBcmds %{buildroot}%{_bindir}/rmnimimage
ln -sf ../bin/xcatDBcmds %{buildroot}%{_bindir}/nimnodeset
ln -sf ../bin/xcatDBcmds %{buildroot}%{_bindir}/nimnodecust
ln -sf ../bin/xcatDBcmds %{buildroot}%{_bindir}/mkdef
ln -sf ../bin/xcatDBcmds %{buildroot}%{_bindir}/chdef
ln -sf ../bin/xcatDBcmds %{buildroot}%{_bindir}/lsdef
ln -sf ../bin/xcatDBcmds %{buildroot}%{_bindir}/rmdef
ln -sf ../bin/xcatDBcmds %{buildroot}%{_bindir}/xcat2nim
ln -sf ../bin/xdsh %{buildroot}%{_bindir}/xdcp
ln -sf ../bin/xcatclientnnr %{buildroot}%{_sbindir}/mknb
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/mkhwconn
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/rmhwconn
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/lshwconn
ln -sf ../bin/xcatclient %{buildroot}%{_bindir}/postage

install -d -pm 755 %{buildroot}%{_sysconfdir}/profile.d
install -D -pm 755 %{S:1} %{buildroot}%{_sysconfdir}/profile.d
install -D -pm 755 %{S:2} %{buildroot}%{_sysconfdir}/profile.d

%files
%doc LICENSE.html
%{_bindir}/*
%{_sbindir}/*
%dir %{_datadir}/xcat
%{_datadir}/xcat/*
%doc %_mandir/*/*
%{_sysconfdir}/profile.d/*
%doc share/doc/*.pdf
%doc share/doc/*.odt
%doc share/doc/*.html
%doc share/doc/*.txt

%changelog
* Wed Nov 24 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.4
- Update from upstream SVN: trunk@8256.

* Mon Nov 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.3
- Update from upstream SVN: trunk@8225.

* Mon Nov 15 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.2
- Update from upstream SVN: trunk@8159.

* Thu Oct 28 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.1
- Update from upstream SVN: trunk@7954.

* Fri Oct 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.4
- Update from upstream SVN: trunk@7904.

* Wed Oct 06 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.3
- Update from upstream SVN: trunk@7759.

* Fri Sep 17 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.2
- Update from upstream SVN: trunk@7490.

* Fri Sep 10 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.1
- Update from upstream SVN: trunk@7385.

* Sun Jun 27 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.3-alt0.1
- Update from upstream SVN: trunk@6611.

* Mon Jun 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.2
- Update from upstream SVN: trunk@6560.

* Wed Jun 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.1
- Update from upstream SVN: trunk@6312.

* Mon May 24 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.4
- Update from upstream SVN: trunk@6208.

* Fri May 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.3
- Update from upstream SVN: trunk@6185.

* Thu Apr 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.2
- Update from upstream SVN: trunk@5831.

* Thu Mar 18 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.1
- Update from upstream SVN: trunk@5517.

* Tue Mar 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.6
- Update from upstream SVN: trunk@5320.

* Fri Feb 05 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.5
- Update from upstream SVN

* Fri Jan 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.4
- Sync with upstream spec file.

* Thu Jan 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.3
- Update from upstream SVN: trunk@5004.

* Tue Jan 19 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.2
- Update from upstream SVN: trunk@4978.

* Mon Jan 11 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.1
- Update from upstream SVN.

* Fri Dec 11 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3.2-alt0.1
- Update from upstream SVN.

* Thu Nov 12 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3-alt0.3
- Update from upstream SVN.

* Tue Nov 03 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3-alt0.2
- Update from upstream SVN.

* Wed Oct 28 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3-alt0.1
- Package for ALT Linux.

