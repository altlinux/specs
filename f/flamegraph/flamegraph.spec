Name: flamegraph
Version: 1.0
Release: alt2
Epoch: 1

Summary: Flame Graphs visualize profiled code-paths
License: CDDL1.0/GPLv2+
Group: Monitoring
URL: http://www.brendangregg.com/flamegraphs.html

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

Conflicts: perl-Devel-NYTProf


%description
Flame Graphs visualize profiled code-paths.

%prep
%setup
%patch0 -p1

%install
mkdir -p %buildroot%_bindir
for file in *.pl *.awk dev/*.pl ;do
install -p -m755 $file %buildroot%_bindir/
done

%files
%_bindir/*
%doc README.md example* demos dev/README

%changelog
* Fri Jan 11 2019 Terechkov Evgenii <evg@altlinux.org> 1:1.0-alt2
- v1.0-13-gf857ebc
- Add Conflicts: to perl-Devel-NYTProf (thanks, repocop)

* Thu Sep 27 2018 Terechkov Evgenii <evg@altlinux.org> 1:1.0-alt1
- v1.0-5-g18c3dea
- Epoch tag added to proper package upgrade

* Wed Aug  2 2017 Terechkov Evgenii <evg@altlinux.org> 20170801-alt1
- git-20170801 (99972c0)

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
