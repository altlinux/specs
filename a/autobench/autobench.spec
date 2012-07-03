Name: autobench
Version: 2.1.2
Release: alt1

Summary:  Utils for automatic benchmarking a web server
License: GPL
Group: Networking/Other

Url: http://www.xenoclast.org/autobench

Source: %name-%version.tar

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
* Fri Feb 20 2009 Denis Klimov <zver@altlinux.org> 2.1.2-alt1
- Initial build for ALT Linux

