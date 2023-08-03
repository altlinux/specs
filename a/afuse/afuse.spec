Name: afuse
Version: 0.5.0
Release: alt1
Summary: Automounting file system implemented in user-space
License: GPLv2
Group: System/Kernel and hardware
URL: https://github.com/pcarrier/%name
Source: %name-%version.tar

BuildRequires: libfuse-devel

%description
%name is an automounting file system implemented in user-space using FUSE.
The advantage of using %name over traditional automounters is %name runs entirely
in user-space by individual users. Thus it can take advantage of the invoking
users environment, for example allowing access to an ssh-agent for password-less
sshfs mounts, or allowing access to a graphical environment to get user input to
complete a mount such as asking for a password.


%prep
%setup -q


%build
%autoreconf
%configure
%make_build


%install
%makeinstall_std


%files
%doc AUTHORS HACKING NEWS README
%_bindir/*


%changelog
* Thu Aug  3 2023 Artyom Bystrov <arbars@altlinux.org> 0.5.0-alt1
- Update to new version

* Mon Sep 02 2013 Led <led@altlinux.ru> 0.4.1-alt1
- 0.4.1
- fixed License
- updated URL

* Wed May 25 2011 Mykola Grechukh <gns@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> - 0.2-5
- Rebuilt with new fuse

* Mon Aug 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.2-4
- fix CVS-2008-2232

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.2-1
- Initial package for Fedora
