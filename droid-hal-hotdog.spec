# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device hotdog
%define vendor oneplus

%define vendor_pretty OnePlus
%define device_pretty 7T Pro

%define installable_zip 1

%define droid_target_aarch64 1

%define makefstab_skip_entries / /product /system /system_ext /vendor
%include rpm/dhd/droid-hal-device.inc

# On Android 8+ the system partition is (intended to be) mounted on /.

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

