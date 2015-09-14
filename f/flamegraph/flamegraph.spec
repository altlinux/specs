Name: flamegraph
Version: 20150915
Release: alt1

Summary: Flame Graphs visualize profiled code-paths
License: CDDL1.0/GPLv2+
Group: Monitoring
URL: http://www.brendangregg.com/flamegraphs.html

BuildArch: noarch

Source0: %name-%version.tar

%description
Flame Graphs visualize profiled code-paths.

%prep
%setup
%install
mkdir -p %buildroot%_bindir
for file in *.pl *.awk dev/*.pl;do
install -p -m755 $file %buildroot%_bindir/
done

%files
%_bindir/*
%doc README.md example-stacks.txt example.svg demos dev/README

%changelog
* Tue Sep 15 2015 Terechkov Evgenii <evg@altlinux.org> 20150915-alt1
- git-20150915

* Sun Aug 16 2015 Terechkov Evgenii <evg@altlinux.org> 20150816-alt1
- git-20150816

* Mon Jul 13 2015 Terechkov Evgenii <evg@altlinux.org> 20150713-alt1
- git-20150713
