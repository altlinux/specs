Name: gfs2-utils
Version: 3.1.8
Release: alt1
License: GPLv2+ and LGPLv2+
Group: System/Kernel and hardware
Summary: Utilities for managing the global file system (GFS2)
URL: https://fedorahosted.org/cluster/wiki/HomePage

Source0: https://fedorahosted.org/released/gfs2-utils/gfs2-utils-%version.tar.gz
Patch0: bz1186515-fsck_gfs2_replace_recent_i_goal_fixes_with_simple_logic.patch
Patch1: bz1202831-mkfs_gfs2_Allow_longer_cluster_names.patch
Patch2: bz1236669-1-fsck_gfs2_Change_duptree_structure_to_have_generic_flags.patch
Patch3: bz1236669-2-fsck_gfs2_Detect_fix_and_clone_duplicate_block_refs_within_a_dinode.patch
Patch4: bz1225634-1-gfs2_utils_Fix_hang_on_withdraw.patch
Patch5: bz1225634-2-scripts_rename_gfs2_wd_udev_sh_to_gfs2_withdraw_helper.patch
Patch6: bz1225634-3-scripts_install_the_withdraw_helper_script.patch
Patch7: bz1225634-4-scripts_install_the_withdraw_udev_rules_script.patch
Patch8: bz1162216-gfs2_edit_savemeta_speed_up_is_block_in_per_node.patch

BuildRequires: flex libblkid-devel libncurses-devel zlib-devel

%description
The gfs2-utils package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in GFS2
file systems.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
%autoreconf
%configure \
	--with-udevdir=/lib/udev
%make_build

%check
%make check

%install
%make -C gfs2 DESTDIR=%buildroot install

%files
%doc doc/COPYING.* doc/COPYRIGHT doc/*.txt doc/README.contributing doc/README.licence doc/README.tests
%_udevrulesdir/82-gfs2-withdraw.rules
%_sbindir/fsck.gfs2
%_sbindir/gfs2_grow
%_sbindir/gfs2_jadd
%_sbindir/mkfs.gfs2
%_sbindir/gfs2_convert
%_sbindir/gfs2_edit
%_sbindir/tunegfs2
%_sbindir/gfs2_withdraw_helper
%_man8dir/fsck.gfs2.8*
%_man8dir/gfs2_grow.8*
%_man8dir/gfs2_jadd.8*
%_man8dir/mkfs.gfs2.8*
%_man8dir/gfs2_convert.8*
%_man8dir/gfs2_edit.8*
%_man8dir/tunegfs2.8*
%_man5dir/*.5*

%changelog
* Thu Mar 31 2016 Valery Inozemtsev <shrek@altlinux.ru> 3.1.8-alt1
- initial release

