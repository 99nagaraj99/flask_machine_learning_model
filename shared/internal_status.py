"""
contains the mapping of status codes, and error messages
"""
from enum import Enum


class StatusCodes(Enum):
    """
    contains the enumeration of status codes
    """

    # IC_1400_COMPANY_ID_MISSING = 1400
    # IC_1401_MACHINE_ID_INCORRECT = 1401
    # IC_1402_CATEGORY_MISSING = 1402
    # IC_1403_START_DATE_MISSING = 1403
    # IC_1404_END_DATE_MISSING = 1404
    # IC_1405_MODEL_ID_MISSING = 1405
    # IC_1406_MACHINE_ID_MISSING = 1406
    # IC_1407_SITE_ID_MISSING = 1407
    # IC_1408_SITE_ID_INCORRECT = 1408
    # IC_1409_MODEL_ID_INCORRECT = 1409
    # IC_1410_COMPANY_ID_INCORRECT = 1410
    # IC_1411_CATEGORY_INCORRECT = 1411
    # IC_1412_DM_ERROR = 1412
    # IC_1413_INVALID_FORMAT = 1413
    # IC_1414_FILTER_MISSING = 1414
    # IC_1415_FILTER_INCORRECT = 1415
    # IC_1416_PATH_PARAMETER_MISSING = 1416
    # IC_1417_DEVICE_ID_INCORRECT = 1417
    # IC_1418_MAKE_ID_INCORRECT = 1418
    # IC_1419_IDENTIFIER_INCORRECT = 1419
    # IC_1420_SERIAL_NUMBER_INCORRECT = 1420
    # IC_1421_EQUIPMENT_RECORD_INCORRECT = 1421
    # IC_1422_SKU_INCORRECT = 1422
    # IC_1423_SKU_ID_INCORRECT = 1423
    # IC_1424_SKU_DESCRIPTION_INCORRECT = 1424
    # IC_1425_RUNNING_HOURS_INCORRECT = 1425
    # IC_1426_MANUFACTURING_DATE_INCORRECT = 1426
    # IC_1427_INITIAL_OPERATION_DATE_INCORRECT = 1427
    # IC_1428_GPS_LOCATION_INCORRECT = 1428
    # IC_1429_GPS_LOCATION_LAT_INCORRECT = 1429
    # IC_1430_GPS_LOCATION_LON_INCORRECT = 1430
    # IC_1431_GPS_LOCATION_RADIUS_INCORRECT = 1431
    # IC_1432_IDENTIFIER_MISSING = 1432
    # IC_1433_SERIAL_NUMBER_MISSING = 1433
    # IC_1434_EQUIPMENT_RECORD_MISSING = 1434
    # IC_1435_SKU_MISSING = 1435
    # IC_1436_SKU_ID_MISSING = 143
    # IC_1437_SKU_DESCRIPTION_MISSING = 1437
    # IC_1438_LABEL1_MISSING = 1438
    # IC_1439_LABEL2_MISSING = 1439
    # IC_1440_BATTERY_TYPE_MISSING = 1440
    # IC_1441_RUNNING_HOURS_MISSING = 1441
    # IC_1442_MANUFACTURING_DATE_MISSING = 1442
    # IC_1443_INITIAL_OPERATION_DATE_MISSING = 1443
    # IC_1444_GPS_LOCATION_MISSING = 1444
    # IC_1445_GPS_LOCATION_LAT_MISSING = 1445
    # IC_1446_GPS_LOCATION_LON_MISSING = 1446
    # IC_1447_GPS_LOCATION_RADIUS_MISSING = 1447
    # IC_1448_LABEL1_INCORRECT = 1448
    # IC_1449_LABEL2_INCORRECT = 1449
    # IC_1450_BATTERY_TYPE_INCORRECT = 1450
    # IC_1451_MAKE_ID_MISSING = 1451
    # IC_1452_DATA_MISSING = 1452
    # IC_1453_DATA_INCORRECT = 1453
    # IC_1454_MACHINE_NOT_PRESENT = 1454
    # IC_1455_MODEL_NOT_PRESENT = 1455
    # IC_1456_MAKE_NOT_PRESENT = 1456
    # IC_1457_NODE_ID_MISSING = 1457
    # IC_1458_NODE_ID_INCORRECT = 1458
    # IC_1459_NODE_ID_LIST_INCORRECT = 1459
    IC_1460_PARAMETER_INCORRECT = 1460
    # IC_1461_SEARCHING_INCORRECT = 1461
    # IC_1462_SORTING_INCORRECT = 1462
    # IC_1463_SORT_FIELD_INCORRECT = 1463
    # IC_1464_SORT_TYPE_INCORRECT = 1464
    # IC_1465_SEARCH_FIELD_INCORRECT = 1465
    # IC_1466_SEARCHING_MISSING = 1466
    # IC_1467_SORTING_MISSING = 1467
    # IC_1468_SORT_FIELD_MISSING = 1468
    # IC_1469_SORT_TYPE_MISSING = 1469
    # IC_1470_SEARCH_FIELD_MISSING = 1470
    # IC_1471_PAGINATION_INCORRECT = 1471
    # IC_1472_PAGINATION_MISSING = 1472
    # IC_1473_PAGE_NUM_INCORRECT = 1473
    # IC_1474_PAGE_NUM__MISSING = 1474
    # IC_1475_PAGE_SIZE_INCORRECT = 1475
    # IC_1476_PAGE_SIZE__MISSING = 1476
    # IC_1477_MIN_THRESHOLD_MISSING = 1477
    # IC_1478_MAX_THRESHOLD_MISSING = 1478
    # IC_1479_MIN_THRESHOLD_INCORRECT = 1479
    # IC_1480_MIN_THRESHOLD_INCORRECT = 1480
    #
    # IC_1490_TIMEPLAN_NAME_MISSING = 1490
    # IC_1491_TIMEPLAN_NAME_INCORRECT = 1491
    # IC_1492_TIMEPLAN_DETAILS_MISSING = 1492
    # IC_1493_TIMEPLAN_DETAILS_INCORRECT = 1493
    # IC_1494_TIMEPLAN_ID_MISSING = 1494
    # IC_1495_TIMEPLAN_ID_INCORRECT = 1495
    #
    # IC_1521_DUPLICATE_EQUIPMENT_RECORD = 1521
    # IC_1522_DUPLICATE_SERIAL_NUMBER = 1522
    # IC_1523_DUPLICATE_DEVICE_ID = 1523
    # IC_1524_WRONG_MODEL_ID = 1524
    #
    # IC_1600_MODEL_NAME_MISSING = 1600
    # IC_1601_MODEL_NAME_INCORRECT = 1601
    # IC_1602_PRICE_MISSING = 1602
    # IC_1603_PRICE_INCORRECT = 1603
    # IC_1604_MODEL_IMAGE_MISSING = 1604
    # IC_1605_MODEL_IMAGE_INCORRECT = 1605
    # IC_1606_THRESHOLD_NAME_MISSING = 1606
    # IC_1607_THRESHOLD_NAME_INCORRECT = 1607
    # IC_1608_THRESHOLD_ID_INCORRECT = 1608
    # IC_1609_THRESHOLD_ACTIVE_MISSING = 1609
    # IC_1610_THRESHOLD_ACIVE_INCORRECT = 1610
    # IC_1611_DEFAULT_THRESHOLD_MISSING = 1611
    # IC_1612_DEFAULT_THRESHOLD_INCORRECT = 1612
    # IC_1613_MACHINE_TYPES_MISSING = 1613
    # IC_1614_MACHINE_TYPES_INCORRECT = 1614
    # IC_1615_INVALID_BOOLEAN_VALUE = 1615
    # IC_1616_INVALID_ACTIVE_VALUE = 1616
    # IC_1617_THRESHOLD_ID_MISSING = 1617

    IC_1620_TYPE_INCORRECT = 1620
    # IC_1621_TYPE_MISSING = 1621
    # IC_1622_NODE_ID_INCORRECT = 1622
    # IC_1623_NODE_ID_MISSING = 1623
    # IC_1624_TIME_FORMAT_INCORRECT = 1624
    # IC_1625_THRESHOLD_NOT_EXIST = 1625
    # IC_1626_THRESHOLD_ASSOCIATED = 1626
    # IC_1627_MODEL_ASSOCIATED = 1627
    # IC_1628_MODEL_NAME_NOT_AVAILABLE = 1628
    #
    # IC_1636_EMAIL_ID_MISSING = 1636
    # IC_1637_USER_ID_INCORRECT = 1637
    #
    # IC_1639_SITE_ID_MISSING = 1639
    # IC_1640_EVENT_MISSING = 1640
    # IC_1641_DUPLICATE_THRESHOLD_NAME = 1641
    # IC_1642_MANUFACTURING_DATE_MORE_THAN_INITIAL_OPERATION_DATE = 1642
    #
    # IC_1700_PAC_ERROR = 1700
    # IC_1701_ORG_ID_MISSING = 1701
    # IC_1702_ORG_ID_INCORRECT = 1702
    #
    # IC_1705_PAGE_INDEX_INVALID = 1705
    # IC_1706_PAGE_SIZE_INVALID = 1706
    # IC_1707_INVALID_DATE_FORMAT = 1707
    #
    # IC_1710_DUPLICATE_SERVICE_NUMBER = 1710
    # IC_1711_ACTIVE_MISSING = 1711
    # IC_1712_ACTIVE_INCORRECT = 1712
    # IC_1713_SERVICE_NUMBER_MISSING = 1713
    # IC_1714_SERVICE_NUMBER_INCORRECT = 1714
    # IC_1715_SERVICE_NAME_MISSING = 1715
    # IC_1716_SERVICE_NAME_INCORRECT = 1716
    # IC_1717_INTERVAL_MISSING = 1717
    # IC_1718_INTERVAL_INCORRECT = 1718
    # IC_1719_NOTES_MISSING = 1719
    # IC_1720_NOTES_INCORRECT = 1720
    # IC_1721_EDITING_MISSING = 1721
    # IC_1722_EDITING_INCORRECT = 1722
    # IC_1723_SERVICE_NUMBER_NOT_UNIQUE = 1723
    # IC_1724_CLIENT_MISSING = 1724
    # IC_1725_CLIENT_INCORRECT = 1725
    # IC_1726_SERVICE_THRESHOLD_ID_NOT_EXIST = 1726
    #
    # IC_4420_ACCESS_DENIED = 4420
    # IC_4421_UNAUTHORIZED = 4421
    # IC_4220_ENTITY_EXIST = 4060
    # IC_4090_NODE_IDS_IN_TIMEPLAN_EXIST = 4090
    # IC_4091_MACHINE_IDS_IN_TIMEPLAN_EXIST = 4091
    # IC_2000_OK = 2000
    # IC_4000_REQUEST_INVALID = 4000
    IC_5000_INTERNAL_ERROR = 5000
    # IC_4010_UNAUTHORIZED = 4010
    # IC_4040_NOT_FOUND = 4040
    #
    # IC_1500_MACHINE_LIST_EMPTY = 1500
    IC_2001_INVALID_VALUE = 2001

    def __str__(self):
        return repr(self.value)


class ErrorMessages(Enum):
    """
    contains the enumeration of error messages
    """
    # IM_1400_COMPANY_ID_MISSING = "Company ID Is Missing"
    # IM_1401_MACHINE_ID_INCORRECT = "Machine IDs are not in expected format"
    # IM_1402_CATEGORY_MISSING = "Category Is Missing"
    # IM_1403_START_DATE_MISSING = "Start is missing"
    # IM_1404_END_DATE_MISSING = "End is missing"
    # IM_1405_MODEL_ID_MISSING = "Model ID Is Missing"
    # IM_1406_MACHINE_ID_MISSING = "Machine ID Is Missing"
    # IM_1407_SITE_ID_MISSING = "Site ID Is Missing"
    # IM_1408_SITE_ID_INCORRECT = "Site IDs are not in expected format"
    # IM_1409_MODEL_ID_INCORRECT = "Model IDs are not in expected format"
    # IM_1410_COMPANY_ID_INCORRECT = "Company ID is not in expected format"
    # IM_1411_CATEGORY_INCORRECT = "Category is not in expected format"
    # IM_1412_DM_ERROR = "DM Error"
    # IM_1413_INVALID_FORMAT = "Invalid Input Format"
    # IM_1414_FILTER_MISSING = "Filter Is Missing"
    # IM_1415_FILTER_INCORRECT = "Filter is not in expected format"
    # IM_1416_PATH_PARAMETER_MISSING = "Path Parameter is missing"
    # IM_1417_DEVICE_ID_INCORRECT = "Device ID Incorrect"
    # IM_1418_MAKE_ID_INCORRECT = "Make ID Incorrect"
    # IM_1419_IDENTIFIER_INCORRECT = "Identifier Incorrect "
    # IM_1420_SERIAL_NUMBER_INCORRECT = "Serial Number Incorrect"
    # IM_1421_EQUIPMENT_RECORD_INCORRECT = "Equipment Record Incorrect"
    # IM_1422_SKU_INCORRECT = "SKU Incorrect"
    # IM_1423_SKU_ID_INCORRECT = "Sku ID Incorrect"
    # IM_1424_SKU_DESCRIPTION_INCORRECT = "SKU description Incorrect"
    # IM_1425_RUNNING_HOURS_INCORRECT = "Running_hours_before_install Incorrect"
    # IM_1426_MANUFACTURING_DATE_INCORRECT = "Manufacturing Date Incorrect"
    # IM_1427_INITIAL_OPERATION_DATE_INCORRECT = "Initial Operation Date Incorrect"
    # IM_1428_GPS_LOCATION_INCORRECT = "GPS Location Incorrect"
    # IM_1429_GPS_LOCATION_LAT_INCORRECT = "Latitude Incorrect"
    # IM_1430_GPS_LOCATION_LON_INCORRECT = "Longitude Incorrect"
    # IM_1431_GPS_LOCATION_RADIUS_INCORRECT = "Radius Incorrect"
    # IM_1432_IDENTIFIER_MISSING = "Identifier Is Missing "
    # IM_1433_SERIAL_NUMBER_MISSING = "Serial Number Is Missing"
    # IM_1434_EQUIPMENT_RECORD_MISSING = "Equipment Record Is Missing"
    # IM_1435_SKU_MISSING = "SKU Is Missing"
    # IM_1436_SKU_ID_MISSING = "Sku ID Is Missing"
    # IM_1437_SKU_DESCRIPTION_MISSING = "SKU description Is Missing"
    # IM_1438_LABEL1_MISSING = "Label1 Is Missing"
    # IM_1439_LABEL2_MISSING = "Label2 Is Missing"
    # IM_1440_BATTERY_TYPE_MISSING = "Battery Type Is Missing"
    # IM_1441_RUNNING_HOURS_MISSING = "Running_hours_before_install Is Missing"
    # IM_1442_MANUFACTURING_DATE_MISSING = "Manufacturing Date Is Missing"
    # IM_1443_INITIAL_OPERATION_DATE_MISSING = "Initial Operation Date Is Missing"
    # IM_1444_GPS_LOCATION_MISSING = "GPS Location Is Missing"
    # IM_1445_GPS_LOCATION_LAT_MISSING = "Latitude Is Missing"
    # IM_1446_GPS_LOCATION_LON_MISSING = "Longitude Is Missing"
    # IM_1447_GPS_LOCATION_RADIUS_MISSING = "Radius Is Missing"
    # IM_1448_LABEL1_INCORRECT = "Label1 Incorrect"
    # IM_1449_LABEL2_INCORRECT = "Label2 Incorrect"
    # IM_1450_BATTERY_TYPE_INCORRECT = "Battery Type Incorrect"
    # IM_1451_MAKE_ID_MISSING = "Make ID Is Missing"
    # IM_1452_DATA_MISSING = "Data Is Missing"
    # IM_1453_DATA_INCORRECT = "Data Incorrect"
    # IM_1454_MACHINE_NOT_PRESENT = "Machine Not Present"
    # IM_1455_MODEL_NOT_PRESENT = "Model Not Present"
    # IM_1456_MAKE_NOT_PRESENT = "Make Not Present"
    # IM_1457_NODE_ID_MISSING = "Node ID Not Present"
    # IM_1458_NODE_ID_INCORRECT = "Node ID Incorrect"
    # IM_1459_NODE_ID_LIST_INCORRECT = "Node ID List Incorrect"
    IM_1460_PARAMETER_INCORRECT = "Parameter Incorrect"
    # IM_1461_SEARCHING_INCORRECT = "Searching Is Incorrect"
    # IM_1462_SORTING_INCORRECT = "Sorting Is Incorrect"
    # IM_1463_SORT_FIELD_INCORRECT = "Sort Field Is Incorrect"
    # IM_1464_SORT_TYPE_INCORRECT = "Sort Type Is Incorrect"
    # IM_1465_SEARCH_FIELD_INCORRECT = "Search Field Is Incorrect"
    # IM_1466_SEARCHING_MISSING = "Searching Is Missing"
    # IM_1467_SORTING_MISSING = "Sorting Is Missing"
    # IM_1468_SORT_FIELD_MISSING = "Sort Field Is Missing"
    # IM_1469_SORT_TYPE_MISSING = "Sort Type Is Missing"
    # IM_1470_SEARCH_FIELD_MISSING = "Search Field Is Missing"
    # IM_1471_PAGINATION_INCORRECT = "Pagination Incorrect"
    # IM_1472_PAGINATION_MISSING = "Pagination Is Missing"
    # IM_1473_PAGE_NUM_INCORRECT = "Page Number Incorrect"
    # IM_1474_PAGE_NUM__MISSING = "Page Number Is Missing"
    # IM_1475_PAGE_SIZE_INCORRECT = "Page Size Incorrect"
    # IM_1476_PAGE_SIZE__MISSING = "Page Size Is Missing"
    # IM_1477_MIN_THRESHOLD_MISSING = "Min Threshold Is Missing"
    # IM_1478_MAX_THRESHOLD_MISSING = "Max Threshold Is Missing"
    # IM_1479_MIN_THRESHOLD_INCORRECT = "Min Threshold Incorrect"
    # IM_1480_MIN_THRESHOLD_INCORRECT = "Max Threshold Incorrect"
    #
    # IM_1490_TIMEPLAN_NAME_MISSING = "Timeplan Name Is Missing"
    # IM_1491_TIMEPLAN_NAME_INCORRECT = "Timeplan Name Is Incorrect"
    # IM_1492_TIMEPLAN_DETAILS_MISSING = "Timeplan Details Missing"
    # IM_1493_TIMEPLAN_DETAILS_INCORRECT = "Timeplan Details Is Incorrect"
    # IM_1494_TIMEPLAN_ID_MISSING = "Timeplan Id Is Missing"
    # IM_1495_TIMEPLAN_ID_INCORRECT = "Timeplan Id Is Incorrect"
    #
    # IM_1600_MODEL_NAME_MISSING = "Model Name Missing"
    # IM_1601_MODEL_NAME_INCORRECT = "Model Name Incorrect"
    # IM_1602_PRICE_MISSING = "Price Missing"
    # IM_1603_PRICE_INCORRECT = "Price Format Incorrect"
    # IM_1604_MODEL_IMAGE_MISSING = "Model Image Missing"
    # IM_1605_MODEL_IMAGE_INCORRECT = "Model Image Incorrect"
    # IM_1606_THRESHOLD_NAME_MISSING = "Threshold Name Missing"
    # IM_1607_THRESHOLD_NAME_INCORRECT = "Threshold Name Incorrect"
    # IM_1608_THRESHOLD_ID_INCORRECT = "Threshold Id Incorrect"
    # IM_1609_THRESHOLD_ACIVE_MISSING = "Threshold Active Missing"
    # IM_1610_THRESHOLD_ACIVE_INCORRECT = "Threshold Active Incorrect"
    # IM_1611_DEFAULT_THRESHOLD_MISSING = "Default Threshold Missing"
    # IM_1612_DEFAULT_THRESHOLD_INCORRECT = "Default Threshold Incorrect"
    # IM_1613_MACHINE_TYPES_MISSING = "Machine Types Missing"
    # IM_1614_MACHINE_TYPES_INCORRECT = "Machine Types Incorrect"
    # IM_1615_INVALID_BOOLEAN_VALUE = "Invalid Boolean Value"
    # IM_1616_INVALID_ACTIVE_VALUE = "Invalid Active Value"
    # IM_1617_THRESHOLD_ID_MISSING = "Threshold Id is Missing"

    IM_1620_TYPE_INCORRECT = "Type is Incorrect"
    # IM_1621_TYPE_MISSING = "Type is Missing"
    # IM_1622_NODE_ID_INCORRECT = "Node Id Incorrect"
    # IM_1623_NODE_ID_MISSING = "Node Id Missing"
    # IM_1624_TIME_FORMAT_INCORRECT = "Time Format Incorrect"
    # IM_1625_THRESHOLD_NOT_EXIST = "Threshold Not Exist"
    # IM_1626_THRESHOLD_ASSOCIATED = "Threshold Already Associated"
    # IM_1627_MODEL_ASSOCIATED = "Machine Associated with Model"
    # IM_1628_MODEL_NAME_NOT_AVAILABLE = "Machine Model Name is Not Available"
    #
    # IM_1636_EMAIL_ID_MISSING = "Email ID Is Missing"
    # IM_1637_USER_ID_INCORRECT = "User ID Incorrect"
    #
    # IM_1639_SITE_ID_MISSING = "Site ID Is Missing"
    # IM_1640_EVENT_MISSING = "Event Is Missing"
    # IM_1641_DUPLICATE_THRESHOLD_NAME = "Threshold with this Name and Company Already Exists"
    # IM_1700_PAC_ERROR = ""
    # IM_1701_ORG_ID_MISSING = "Organization ID Is Missing"
    # IM_1702_ORG_ID_INCORRECT = "Organization ID is not in expected format"
    #
    # IM_1710_DUPLICATE_SERVICE_NUMBER = "Duplicate Service Record"
    # IM_1711_ACTIVE_MISSING = "Active missing"
    # IM_1712_ACTIVE_INCORRECT = "Active incorrect"
    # IM_1713_SERVICE_NUMBER_MISSING = "Service number missing"
    # IM_1714_SERVICE_NUMBER_INCORRECT = "Service number incorrect"
    # IM_1715_SERVICE_NAME_MISSING = "Service name missing"
    # IM_1716_SERVICE_NAME_INCORRECT = "Service name incorrect"
    # IM_1717_INTERVAL_MISSING = "Interval missing"
    # IM_1718_INTERVAL_INCORRECT = "Interval incorrect"
    # IM_1719_NOTES_MISSING = "Notes missing"
    # IM_1720_NOTES_INCORRECT = "Notes incorrect"
    # IM_1721_EDITING_MISSING = "Editing missing"
    # IM_1722_EDITING_INCORRECT = "Editing incorrect"
    # IM_1723_SERVICE_NUMBER_NOT_UNIQUE = "Service Number should be unique"
    # IM_1724_CLIENT_MISSING = "Client missing"
    # IM_1725_CLIENT_INCORRECT = "Client incorrect"
    # IM_1726_SERVICE_THRESHOLD_ID_NOT_EXIST = "Service threshold not exist"
    # IM_4420_ACCESS_DENIED = "Access Denied"
    # IM_4421_UNAUTHORIZED = "Unauthorized"
    IM_5000_INTERNAL_ERROR = "Internal server error"
    #
    #
    # IM_1500_MACHINE_LIST_EMPTY = "Machine List is empty"
    IM_2001_INVALID_VALUE = "Invalid value"

    def __str__(self):
        return repr(self.value)


class FixedValues(Enum):
    """
    defines enumeration of machine event
    """
    C_HIGH_USAGE_MACHINES = 'hu'
    C_LOW_USAGE_MACHINES = 'lu'
    C_ALL_MACHINES = 'all'
    C_OUT_OF_FENCE_MACHINES = 'gf'
    C_NO_SIGNAL_MACHINES_ERROR = 'ne'
    C_NO_SIGNAL_MACHINES_BATTERY = 'nb'
    C_NO_USAGE_MACHINES = 'nu'
    C_BATTERY_ISSUES_MACHINES = 'bi'
    C_CRASH_ISSUES_MACHINES = 'ci'
    C_FACILITIES_MACHINE = 'fa'

    def __str__(self):
        return repr(self.value)


class OperationTypes(Enum):
    """
    defines the operation types for Master History Tables
    """
    H_UPDATED_DATA = "Updated"
    H_DELETED_DATA = "Deleted"
    H_CREATED_DATA = "Created"

    def __str__(self):
        return repr(self.value)
