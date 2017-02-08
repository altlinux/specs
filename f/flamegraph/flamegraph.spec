Name: flamegraph
Version: 20170208
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
for file in *.pl *.awk dev/*.pl dev/*.py;do
install -p -m755 $file %buildroot%_bindir/
done

%files
%_bindir/*
%doc README.md example* demos dev/README dev/*.d

%changelog
* Wed Feb  8 2017 Terechkov Evgenii <evg@altlinux.org> 20170208-alt1
- git-20170208 (54b5f97)

* Thu Jan 28 2016 Terechkov Evgenii <evg@altlinux.org> 20160128-alt1
- git-20160128

* Sat Nov 14 2015 Terechkov Evgenii <evg@altlinux.org> 20151114-alt1
- git-20151114

* Tue Sep 15 2015 Terechkov Evgenii <evg@altlinux.org> 20150915-alt1
- git-20150915

* Sun Aug 16 2015 Terechkov Evgenii <evg@altlinux.org> 20150816-alt1
- git-20150816

* Mon Jul 13 2015 Terechkov Evgenii <evg@altlinux.org> 20150713-alt1
- git-20150713
