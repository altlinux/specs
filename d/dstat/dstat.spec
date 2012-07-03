Name: dstat
Version: 0.7.2
Release: alt1.1

Summary: Versatile vmstat, iostat and ifstat replacement
License: GPL
Group: Monitoring

URL: http://dag.wieers.com/home-made/dstat
Packager: Michael Shigorin <mike@altlinux.org>
Source: %url/%name-%version.tar.bz2

Requires: python
BuildArch: noarch

# Automatically added by buildreq on Sat Jul 23 2005 (-bi)
BuildRequires: python-base python-modules-compiler python-modules-encodings rpm-build-python

%description
Dstat is a versatile replacement for vmstat, iostat and ifstat.
It overcomes some of the limitations and adds some extra features.

Dstat allows you to view all of your system resources instantly,
you can eg. compare disk usage in combination with interrupts from
your IDE controller, or compare the network bandwidth numbers
directly with the disk throughput (in the same interval).

Dstat also cleverly gives you the most detailed information in
columns and clearly indicates in what magnitude and unit the output
is displayed. Less confusion, less mistakes.

Dstat is also unique in letting you aggregate block device throughput
for a certain diskset or network bandwidth for a group of interfaces,
ie. you can see the throughput for all the block devices that make up
a single filesystem or storage system.

You can customize your dstat output from /etc/dstat.conf and you can
write your own dstat modules to plug into the dstat output.

Dstat's output, in its current form, is not very useful to be post-
processed by other tools. It's mostly meant for allowing humans to
interprete real-time data as easy as possible.

%prep
%setup

%build
%install
%makeinstall

%files
%doc AUTHORS ChangeLog README TODO 
%doc %_man1dir/*
#%config(noreplace) %_sysconfdir/dstat.conf
%_bindir/*
%_datadir/%name/

# FIXME:
# - dstat -dfncl bails out with division by zero!

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Michael Shigorin <mike@altlinux.org> 0.7.2-alt1
- 0.7.2 (thx ru_classic@)

* Wed May 05 2010 Michael Shigorin <mike@altlinux.org> 0.7.1-alt1
- 0.7.1 (closes: #23415)

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt1.2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.6.6-alt1.1
- Rebuilt with python-2.5.

* Sun Apr 29 2007 Michael Shigorin <mike@altlinux.org> 0.6.6-alt1
- 0.6.6 (minor fixes/enhancements)

* Tue Dec 12 2006 Michael Shigorin <mike@altlinux.org> 0.6.4-alt1
- 0.6.4
  + added openvz plugins

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 0.6.3-alt1
- 0.6.3

* Wed Jan 25 2006 Michael Shigorin <mike@altlinux.org> 0.6.1-alt1
- 0.6.1

* Sat Jul 23 2005 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- 0.6.0

* Tue Mar 15 2005 Michael Shigorin <mike@altlinux.ru> 0.5.8-alt1
- built for ALT Linux

* Thu Nov 11 2004 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Tue Oct 26 2004 Dag Wieers <dag@wieers.com> - 0.4-1
- Initial package. (using DAR)
