Name: autobench
Version: 2.1.2
Release: alt1.qa2

Summary:  Utils for automatic benchmarking a web server
License: GPL
Group: Networking/Other

Url: http://www.xenoclast.org/autobench

Source: %name-%version.tar
Patch: autobench-2.1.2-alt-perl522.patch

Requires: httperf gnuplot

%description
Autobench is a simple Perl script for automating the process of
benchmarking a web server (or for conducting a comparative test of
two different web servers). The script is a wrapper around  httperf.
Autobench runs httperf a number of times against each host,
increasing the number of requested connections per second on each
iteration, and extracts the significant data from the httperf output,
delivering a CSV or TSV format file which can be imported directly
into a spreadsheet for analysis/graphing. 

%prep
%setup
%patch -p2

%build
%make_build

%install
%make_install	PREFIX=%buildroot \
		ROOTMAN_PREFIX=%_datadir \
		ROOTBIN_PREFIX=/usr \
		AB_CFG=%_sysconfdir/autobench.conf install

%files
%doc README ChangeLog
%_bindir/autobench*
%_bindir/bench2graph
%_bindir/crfile
%_bindir/sesslog

%_sysconfdir/%name.conf
%_man1dir/*


%changelog
* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1.qa2
- NMU: fix for perl 5.22

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.1.2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Feb 20 2009 Denis Klimov <zver@altlinux.org> 2.1.2-alt1
- Initial build for ALT Linux

