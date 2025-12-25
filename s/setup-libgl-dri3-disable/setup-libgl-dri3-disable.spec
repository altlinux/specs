Name: setup-libgl-dri3-disable
Version: 0.2
Release: alt2

Summary: LIBGL_DRI3_DISABLE=true
License: public domain
Group: System/Configuration/Hardware

Url: http://mesa3d.org/envvars.html
BuildArch: noarch

%define proffile %_sysconfdir/profile.d/libgl-dri3-disable.sh

%description
Set %summary to help gtk3 apps work with selinux...

Suggested-by: nbr@

...and to reduce probability of intel/amdgpu videodriver/firmware crashes
like this (at the cost of reduced performance):

amdgpu 0000:07:00.0: amdgpu: GPU reset(1) succeeded!
amdgpu 0000:07:00.0: [drm] *ERROR* flip_done timed out

See-also:
http://community.frame.work/t/responded-flip-done-timed-out-errors-being-printed-to-console-after-ubuntu-update/40025/3
http://gitlab.freedesktop.org/drm/amd/-/issues/1707
http://github.com/ROCm/amdgpu/issues/22

%prep

%build
cat > libgl-dri3-disable.sh << EOF
if [ -n "\$DISPLAY" ]; then
	export LIBGL_DRI3_DISABLE=true
fi
EOF

%install
install -pDm755 libgl-dri3-disable.sh %buildroot%proffile

%files
%config(noreplace) %proffile

%changelog
* Thu Dec 25 2025 Michael Shigorin <mike@altlinux.org> 0.2-alt2
- improve description to also mention intel/amdgpu's "flip_done timed out"

* Mon Jul 02 2018 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- brown paper bag bugfix (thx nbr)

* Thu Jun 28 2018 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

